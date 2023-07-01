import numpy as np
from flojoy import flojoy, DataContainer, DefaultParams
from node_sdk.small_memory import SmallMemory

memory_key = "SECOND_ORDER_SYSTEM"


@flojoy
def SECOND_ORDER_SYSTEM(
    default: DataContainer,
    default_params: DefaultParams,
    d1: float = 250,
    d2: float = 100,
) -> DataContainer:
    """The SECOND_ORDER_SYSTEM has a second order exponential function.
    This node is designed to be used in a loop.
    The data is appended as the loop progress and written to memory.

    Parameters
    ----------
    d1: float
        The first time constant.
    d2: float
        The second time constant.

    Returns
    -------
    dataframe
        The most recent value of the second order function.
    """
    node_id = params.get("node_id", 0)
    x1 = np.exp(-1.0 / d1) if d1 > 0 else 0.0
    x2 = np.exp(-1.0 / d2) if d2 > 0 else 0.0
    ac = (1.0 - x1) * (1.0 - x2)
    bpd = x1 + x2
    bd = x1 * x2
    data = SmallMemory().read_memory(node_id, memory_key)
    if data is None:
        initialize = True
    elif type(data) == np.ndarray:
        initialize = False
    else:
        raise TypeError(f"Error loading object from REDIS. Type: {type(data)}")
    y_primes = np.zeros((2, 1)) if initialize else data[::-1]
    response = ac * dc_inputs[0].y[-1] + bpd * y_primes[0] - bd * y_primes[1]
    y_primes[1] = y_primes[0]
    y_primes = np.insert(y_primes, 0, response)
    SmallMemory().write_to_memory(node_id, memory_key, y_primes[::-1])
    return DataContainer(
        x=dc_inputs[0].y, y=np.ones_like(dc_inputs[0].y) * float(y_primes[0])
    )
