import numpy as np
from flojoy import flojoy, Vector, OrderedPair
from typing import Optional


@flojoy
def CONSTANT(
    default: Optional[Vector] = None, constant: float = 3.0, step: int = 1000
) -> OrderedPair:
    """Generates a single x-y vector of numeric (floating point) constants"""
    if default:
        x = default.v
    x = np.arange(0, step, 1)  # type: ignore

    y = np.full(len(x), constant)
    return OrderedPair(x=x, y=y)
