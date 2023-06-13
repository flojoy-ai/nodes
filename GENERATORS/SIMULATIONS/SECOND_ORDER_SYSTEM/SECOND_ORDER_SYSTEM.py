import numpy as np
from flojoy import flojoy, DataContainer
from node_sdk.small_memory import SmallMemory

memory_key = "SECOND_ORDER_SYSTEM"


@flojoy
def SECOND_ORDER_SYSTEM(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    # Let's first define things that won't change over
    # each iteration: time constants, etc ...
    d1 = params["d1"]  # first time constant in us, 250
    d2 = params["d2"]  # second time constant in us, 100
    node_id = params.get("node_id", 0)

    # ... and now some helper functions
    x1 = np.exp(-1.0 / d1) if d1 > 0 else 0.0
    x2 = np.exp(-1.0 / d2) if d2 > 0 else 0.0
    ac = (1.0 - x1) * (1.0 - x2)
    bpd = x1 + x2
    bd = x1 * x2

    # Now we require memory. The only thing we need in memory is the last two
    # values the system had in this basic example.
    data = SmallMemory().read_memory(node_id, memory_key)
    print('debug: ', type(data))
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
    response = ac * dc_inputs[0].y[-1] + bpd * y_primes[0] - bd * y_primes[1]
    y_primes[1] = y_primes[0]

    # prepend the most recent result to the front of the histrory
    y_primes = np.insert(y_primes, 0, response)
    # We now write to memory, reversing the order ...
    SmallMemory().write_to_memory(node_id, memory_key, y_primes[::-1])
    # ... and return the result!
    return DataContainer(
        x=dc_inputs[0].y, y=np.ones_like(dc_inputs[0].y) * float(y_primes[0])
    )  # returns input output pair
