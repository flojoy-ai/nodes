import numpy as np
from flojoy import flojoy, OrderedPair, Vector, Scalar


@flojoy
def ABS(default: OrderedPair | Vector | Scalar) -> OrderedPair:
    """The ABS node returns an absolute value."""

    match default:
        case OrderedPair():
            x = default.x
            y = np.abs(default.y)
        case Scalar():
            x = default.c
            y = np.abs(x)
        case Vector():
            x = default.v
            y = np.abs(x)

    return OrderedPair(x=x, y=y)
