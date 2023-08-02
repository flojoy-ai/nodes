import numpy as np
from flojoy import DCNpArrayType, flojoy, Vector, OrderedPair
from typing import Optional


@flojoy
def CONSTANT(
    default: Optional[Vector | OrderedPair] = None,
    constant: float = 3.0,
    step: int = 1000,
) -> OrderedPair:
    """Generates a single x-y vector of numeric (floating point) constants"""

    if not default:
        x = np.arange(0, step, 1)
    else:
        match default.type:
            case "ordered_pair":
                x = default.y
            case "vector":
                x = default.v

    y = np.full(len(x), constant)

    return OrderedPair(x=x, y=y)
