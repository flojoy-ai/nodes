import numpy as np
from flojoy import OrderedPair, flojoy, DataContainer


@flojoy(node_type="SIMULATION")
def RAND(default: OrderedPair) -> OrderedPair:
    x = default.y
    y = np.random.normal(size=len(x))

    return OrderedPair(x=x, y=y)


@flojoy
def RAND_MOCK(default: OrderedPair) -> OrderedPair:
    x = default.y
    y = x

    # for reproducibility returning an array with constant values
    return OrderedPair(x=x, y=y)
