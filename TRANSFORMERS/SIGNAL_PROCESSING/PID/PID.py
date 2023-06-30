import numpy as np
from flojoy import flojoy, DataContainer, DefaultParams
from node_sdk.small_memory import SmallMemory
memory_key = 'pid-info'

@flojoy
def PID(default: DataContainer, default_parmas: DefaultParams, Kp: float=5, Ki: float=0.0143, Kd: float=356.25) -> DataContainer:
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
    Kp: float = params['Kp']
    Ki: float = params['Ki']
    Kd: float = params['Kd']
    node_id = params.get('node_id', 0)
    data = SmallMemory().read_memory(node_id, memory_key)
    if data is None:
        initialize = True
    elif type(data) == np.ndarray:
        initialize = False
    else:
        raise TypeError('Issue reading memory from REDIS.')
    integral: int = 0 if initialize else data[0]
    regulation_error_primes = np.zeros((3, 1)) if initialize else data[1:]
    print(f'Recovered data: {data}')
    regulation_error = dc_inputs[0].y[-1]
    integral: float = integral + 0.5 * Ki * (regulation_error + regulation_error_primes[0])
    output_signal = Kp * regulation_error + integral + 0.1667 * Kd * (regulation_error - regulation_error_primes[2] + 3.0 * (regulation_error_primes[0] - regulation_error_primes[1]))
    regulation_error_primes[2]: float = regulation_error_primes[1]
    regulation_error_primes[1]: float = regulation_error_primes[0]
    regulation_error_primes[0]: float = regulation_error
    SmallMemory().write_to_memory(node_id, memory_key, np.append(integral, regulation_error_primes))
    print(regulation_error, output_signal)
    return DataContainer(x=dc_inputs[0].y, y=np.ones_like(dc_inputs[0].y) * output_signal)