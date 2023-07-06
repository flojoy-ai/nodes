import numpy as np
from flojoy import OrderedPair, flojoy
from functools import reduce


@flojoy
def MULTIPLY(a: OrderedPair, b: OrderedPair) -> OrderedPair:
    """Takes 2 input vectors, multiplies them, and returns the result"""
    x = a.x

    y = reduce(lambda u, v: np.multiply(u, v.y), b, a.y)

    return OrderedPair(x=x, y=y)
