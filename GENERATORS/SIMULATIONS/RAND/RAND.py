import numpy as np
from flojoy import OrderedPair, flojoy


@flojoy
def RAND(default: OrderedPair) -> OrderedPair:
    x = default.y
    y = np.random.normal(size=len(x))
    return OrderedPair(x=x, y=y)


@flojoy
def RAND_MOCK(default: OrderedPair) -> OrderedPair:
    x = default.y
    y = x
    return OrderedPair(x=x, y=y)
