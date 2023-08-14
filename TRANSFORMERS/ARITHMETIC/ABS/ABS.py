import numpy as np
from flojoy import flojoy, OrderedPair, Vector, Scalar


@flojoy
def ABS(default: OrderedPair | Vector | Scalar) -> OrderedPair:
    """The ABS node take a numeric array, a vector, or a scalar as input and returns its absolute value.

    Inputs
    ------
    default : OrderedPair|Vector|Scalar
        The input to apply the absolute value to.

    Returns
    -------
    OrderedPair
        x: the x-axis of the input.
        y: the absolute value of the input.
    """

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
