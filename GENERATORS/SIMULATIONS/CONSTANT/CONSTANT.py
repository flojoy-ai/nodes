import numpy as np
from flojoy import flojoy, Vector, OrderedPair, Scalar
from typing import Optional


@flojoy
def CONSTANT(default: Optional[Vector] = None, constant: float = 3.0) -> OrderedPair | Scalar:
    """The CONSTANT node generates a single x-y vector of numeric (floating point) constants
    if there's an input vector, otherwise the constant node will generate a scalar value

    Parameters
    ----------
    constant : float

    Returns
    -------
    OrderedPair|Scalar
        OrderedPair if there's an input
        x: input vector
        y: constant with the size of the input vector
        Scalar if no input
        c: constant
    """
    if default:
        x = default.v
        y = np.full(len(x), constant)
        return OrderedPair(x=x, y=y)
    return Scalar(c=constant)
