import os
import sys
import inspect
import subprocess
import multiprocessing
import cloudpickle
import venv

from functools import  wraps

class MultiprocessingExecutableContextManager:
    """Temporarily change the executable used by multiprocessing."""
    def __init__(self, executable_path):
        self.original_executable_path = sys.executable
        self.executable_path = executable_path

    def __enter__(self):
        self.original_start_method = multiprocessing.get_start_method()
        multiprocessing.set_executable(self.executable_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        multiprocessing.set_executable(self.original_executable_path)

class SwapSysPath:
    """Temporarily swap the sys.path of the child process with the sys.path of the parent process."""
    def __init__(self, venv_executable):
        self.new_path = _get_venv_syspath(venv_executable)
        self.old_path = None

    def __enter__(self):
        self.old_path = sys.path
        sys.path = self.new_path

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.path = self.old_path


def _install_pip_dependencies(venv_executable: os.PathLike, pip_dependencies: tuple[str]):
    """Install pip dependencies into the virtual environment."""
    command = [venv_executable, "-m", "pip", "install"] + list(pip_dependencies)
    subprocess.check_call(command)

def _get_venv_syspath(venv_executable: os.PathLike) -> list[str]:
    """Get the sys.path of the virtual environment."""
    command = [venv_executable, "-c", "import sys\nprint(sys.path)"]
    cmd_output = subprocess.run(command, check=True, capture_output=True, text=True)
    return eval(cmd_output.stdout)

class PickleableFunctionWithPipeIO:
    """A wrapper for a function that can be pickled and executed in a child process."""
    def __init__(self, func, child_conn, venv_executable):
        self._func_serialized = cloudpickle.dumps(func)
        self._child_conn = child_conn
        self._venv_executable = venv_executable

    def __call__(self, *args, **kwargs):
        fn = cloudpickle.loads(self._func_serialized)
        args = [cloudpickle.loads(arg) for arg in args]
        kwargs = {key: cloudpickle.loads(value) for key, value in kwargs.items()}
        with SwapSysPath(venv_executable=self._venv_executable):
            result = fn(*args, **kwargs)
        self._child_conn.send(result)

def run_in_venv(pip_dependencies=[]):
    pip_dependencies = ["flojoy", "cloudpickle"] + pip_dependencies
    # Get the path from where this functino was called
    node_dirpath = os.path.dirname(inspect.stack()[1].filename)
    venv_path = os.path.join(node_dirpath, "node_env")
    venv_executable = os.path.join(venv_path, "bin", "python")
    # Create the node_env virtual environment if it does not exist
    if not os.path.exists(venv_path):
        venv.create(venv_path, with_pip=True)

    # Install the pip dependencies into the virtual environment
    if pip_dependencies:
        _install_pip_dependencies(venv_executable=venv_executable, pip_dependencies=tuple(pip_dependencies))

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Serialize function arguments using cloudpickle
            parent_conn, child_conn = multiprocessing.Pipe()
            args = [cloudpickle.dumps(arg) for arg in args]
            kwargs = {key: cloudpickle.dumps(value) for key, value in kwargs.items()}
            pickleable_func_with_queue = PickleableFunctionWithPipeIO(func, child_conn, venv_executable)
            # Start the context manager that will change the executable used by multiprocessing
            with MultiprocessingExecutableContextManager(venv_executable):
                # Create a new process that will run the Python code
                process = multiprocessing.Process(target=pickleable_func_with_queue, args=args, kwargs=kwargs)
                # Start the process
                process.start()
                # Fetch result from the child process
                serialized_result = parent_conn.recv_bytes()
                # Wait for the process to finish
                process.join()
            # Check if the process exited with an error
            if process.exitcode != 0:
                raise ChildProcessError(f"Process exited with code {process.exitcode}")
            # Check if the serialized_result is empty
            if not serialized_result:
                raise RuntimeError(f"No result was returned for {func.__name__}")
            # Deserialize the result using cloudpickle
            return cloudpickle.loads(serialized_result)
        return wrapper

    return decorator