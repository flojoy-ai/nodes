import numpy as np
from flojoy import flojoy, OrderedPair, DefaultParams
from node_sdk.small_memory import SmallMemory

memory_key = "pid-info"


@flojoy(inject_node_metadata=True)
def PID(
    default: OrderedPair,
    default_params: DefaultParams,
    Kp: float = 5,
    Ki: float = 0.0143,
    Kd: float = 356.25,
) -> OrderedPair:
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
    OrderedPair
        The dataframe modified according to the PID.
    """

    # First let's get the parameters that won't change
    node_id = default_params.node_id
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

    regulation_error = default.y[
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
    return OrderedPair(x=default.y, y=np.ones_like(default.y) * output_signal)
