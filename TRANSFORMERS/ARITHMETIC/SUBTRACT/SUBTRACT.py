import numpy as np
from flojoy import flojoy, OrderedPair
from functools import reduce


@flojoy
def SUBTRACT(a: OrderedPair, b: OrderedPair) -> OrderedPair:
    """Subtract 2 input vectors and return the result"""
    x = a.x

    y = reduce(lambda u, v: np.subtract(u, v.y), b, a.y)

    return OrderedPair(x=x, y=y)
