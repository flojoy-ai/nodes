import numpy as np
from flojoy import flojoy, OrderedPair, DefaultParams
from node_sdk.small_memory import SmallMemory

memory_key = "SECOND_ORDER_SYSTEM"


@flojoy(inject_node_metadata=True)
def SECOND_ORDER_SYSTEM(
    default: OrderedPair,
    default_params: DefaultParams,
    d1: float = 250,
    d2: float = 100,
) -> OrderedPair:
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
    OrderedPair
        The most recent value of the second order function.
    """

    # Let's first define things that won't change over
    # each iteration: time constants, etc ...

    node_id = default_params.node_id

    # ... and now some helper functions
    x1 = np.exp(-1.0 / d1) if d1 > 0 else 0.0
    x2 = np.exp(-1.0 / d2) if d2 > 0 else 0.0
    ac = (1.0 - x1) * (1.0 - x2)
    bpd = x1 + x2
    bd = x1 * x2

    # Now we require memory. The only thing we need in memory is the last two
    # values the system had in this basic example.
    data = SmallMemory().read_memory(node_id, memory_key)
    if data is None:
        initialize = True
    elif type(data) == np.ndarray:
        initialize = False
    else:
        raise TypeError(f"Error loading object from REDIS. Type: {type(data)}")

    # We're going to store and read the data in reverse order to
    # how it is accessed here. We will write the functionality
    # below to assume the most recent time step is the first
    # index. However, for visualization and external access,
    # it makes the most sense to have the first time step
    # as the first index!
    y_primes = np.zeros((2, 1)) if initialize else data[::-1]

    # Using input from controller as v[0].y ...
    response = ac * default.y[-1] + bpd * y_primes[0] - bd * y_primes[1]
    y_primes[1] = y_primes[0]

    # prepend the most recent result to the front of the histrory
    y_primes = np.insert(y_primes, 0, response)
    # We now write to memory, reversing the order ...
    SmallMemory().write_to_memory(node_id, memory_key, y_primes[::-1])
    # ... and return the result!
    return OrderedPair(
        x=default.y, y=np.ones_like(default.y) * float(y_primes[0])
    )  # returns input output pair
