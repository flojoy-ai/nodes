from typing import Optional
import numpy as np
from flojoy import Vector, flojoy, OrderedPair

@flojoy
def CONSTANT(
    default: Optional[Vector | OrderedPair] = None,
    constant: float = 3.0,
    step: float = 1000,
) -> OrderedPair:
    """Generates a single x-y vector of numeric (floating point) constants"""

    if default:
        x = default.v
    else:
        x = np.arange(0, step, 1)

    y = np.full(len(x), constant)

    return OrderedPair(x=x, y=y)
