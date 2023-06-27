from typing import Callable

import os
import sys
import inspect
import subprocess
import cloudpickle
import venv

from functools import wraps
from textwrap import dedent, indent



def _get_source(func: Callable) -> str:
    lines = inspect.getsource(func).split("\n")
    while not lines[0].startswith("def"):
        lines.pop(0)
    return "\n".join(lines)

def _generate_code(func: Callable) -> str:
    source = _get_source(func)
    script_code =  f'''\
    import os
    import sys
    import io
    import contextlib
    import cloudpickle
    from flojoy import DataContainer

{indent(source, "    ", )}

    def main():
        input_objects = cloudpickle.loads(sys.stdin.buffer.read())
        args, kwargs = input_objects["args"], input_objects["kwargs"]
        result = {func.__name__}(*args, **kwargs)
        return result, cloudpickle.dumps(result)
        

    with contextlib.redirect_stdout(sys.stderr):
        result, result_buff = main()
    sys.stdout.buffer.write(result_buff)
    '''
    return dedent(script_code)

def _run_inputless_command_from_venv(venv_path: str, command: list[str]):
    command = [os.path.join(venv_path, "bin", "python"), "-m"] + command
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    output = b""
    while True:
        # Read the output of the subprocess in chunks
        chunk = process.stdout.read(1024)
        if not chunk:
            break
        # Write the output of the subprocess to the host's stdout
        sys.stdout.buffer.write(chunk)
        sys.stdout.flush()
    process.wait()

def _run_python_script_as_subprocess(venv_path: os.PathLike, script_code: str, serialized_inputs: bytes) -> bytes:
    """Run a python script within a subprocess, given a virtual environment."""
    command = [os.path.join(venv_path, "bin", "python"), "-c", script_code]
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    serialized_output, process_stderr = process.communicate(serialized_inputs)
    if(process_stderr is not None):
        sys.stdout.buffer.write(process_stderr)
        sys.stdout.flush()
    # Check if the subprocess exited with an error
    if process.returncode != 0:
        raise ChildProcessError(f"Subprocess exited with code {process.returncode}")
    # Read the output from stdout
    return serialized_output

def run_in_venv(pip_dependencies=[]):
    pip_dependencies = ["flojoy", "cloudpickle"] + pip_dependencies

    def decorator(func):
        venv_path = os.path.join(
            os.path.dirname(inspect.getfile(func)),
            "node_env"
        )
        # Create the node_env virtual environment if it does not exist
        if not os.path.exists(venv_path):
            venv.create(venv_path, with_pip=True)
        # Install the pip dependencies from the pip_dependencies list all at once

        if pip_dependencies:
            _run_inputless_command_from_venv(venv_path=venv_path, command=["pip", "install"] + pip_dependencies)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Serialize function arguments using cloudpickle
            serialized_inputs = cloudpickle.dumps({
                "args": args,
                "kwargs": kwargs
            })
            # Define the Python code to be run
            script_code = _generate_code(func)
            # Run the Python code in a separate Python interpreter and capture the output
            script_serialized_output = _run_python_script_as_subprocess(venv_path=venv_path, script_code=script_code, serialized_inputs=serialized_inputs)
            # Deserialize the function's result using cloudpickle
            return cloudpickle.loads(script_serialized_output)

        return wrapper

    return decorator
