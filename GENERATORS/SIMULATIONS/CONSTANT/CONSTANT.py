import numpy as np
from flojoy import DCNpArrayType, flojoy, Vector, OrderedPair
from typing import Optional


@flojoy
def CONSTANT(
    default: Optional[Vector | OrderedPair] = None,
    constant: float = 3.0,
    step: float = 1000,
) -> OrderedPair:
    """
    The CONSTANT node generates a single x-y vector of numeric (floating point) constants.
    """

    x = np.arange(0, step, 1)
    if default:
        match default:
            case OrderedPair():
                x = default.y
            case Vector():
                x = default.v

    y = np.full(len(x), constant)

    return OrderedPair(x=x, y=y)
