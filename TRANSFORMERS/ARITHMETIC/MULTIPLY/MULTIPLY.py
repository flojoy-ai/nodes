import numpy as np
from flojoy import OrderedPair, flojoy  # type:ignore


@flojoy
def MULTIPLY(
    a: OrderedPair,
    b: OrderedPair,
) -> OrderedPair:
    """Takes 2 input vectors, multiplies them, and returns the result"""
    x = a.x
    u = a.y
    v = b.y
    y = np.multiply(u, v)
    return OrderedPair(x=x, y=y)
