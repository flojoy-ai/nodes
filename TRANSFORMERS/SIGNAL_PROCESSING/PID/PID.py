import numpy as np
from flojoy import flojoy, DataContainer
from flojoy.small_memory import SmallMemory

memory_key = "pid-info"


@flojoy
def PID(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The PID node acts like a PID function.
    The returned value with be modified according to the
    PID parameters Kp, Ki, and Kd.

    Parameters
    ----------
    Kp: float
        The proprotional PID parameter.
    Ki: float
        The integral PID parameter.
    Kd: float
        The derivative PID parameter.

    Returns
    -------
    dataframe
        The dataframe modified according to the PID. Ordered pair.
    """

    # First let's get the parameters that won't change
    Kp: float = params["Kp"]
    Ki: float = params["Ki"]
    Kd: float = params["Kd"]
    node_id = params.get("node_id", 0)
    # Now we need some memory! We need to keep track of the running
    # integral value of the inputs (regulation errors), as well as
    # the previous 3 values of the regulation error
    data = SmallMemory().read_memory(node_id, memory_key)
    if data is None:
        initialize = True
    elif type(data) == np.ndarray:
        initialize = False
    else:
        raise TypeError("Issue reading memory from REDIS.")
    integral: int = 0 if initialize else data[0]
    regulation_error_primes = np.zeros((3, 1)) if initialize else data[1:]
    print(f"Recovered data: {data}")

    regulation_error = dc_inputs[0].y[
        -1
    ]  # constant node makes long list of items; just need the value so take last element
    integral: float = integral + 0.5 * Ki * (
        regulation_error + regulation_error_primes[0]
    )
    output_signal = (
        Kp * regulation_error
        + integral
        + 0.1667
        * Kd
        * (
            regulation_error
            - regulation_error_primes[2]
            + 3.0 * (regulation_error_primes[0] - regulation_error_primes[1])
        )
    )
    regulation_error_primes[2]: float = regulation_error_primes[1]
    regulation_error_primes[1]: float = regulation_error_primes[0]
    regulation_error_primes[0]: float = regulation_error

    # Now write to memory ...
    SmallMemory().write_to_memory(
        node_id, memory_key, np.append(integral, regulation_error_primes)
    )
    print(regulation_error, output_signal)
    # ... and return the result
    return DataContainer(
        x=dc_inputs[0].y, y=np.ones_like(dc_inputs[0].y) * output_signal
    )
