import numpy as np
from flojoy import flojoy, OrderedPair


@flojoy
def CONSTANT(default: OrderedPair, constant: float = 3.0) -> OrderedPair:
    """Generates a single x-y vector of numeric (floating point) constants"""
    x = default.y
    y = np.full(len(x), constant)
    return OrderedPair(x=x, y=y)
