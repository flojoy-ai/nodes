from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.signal


@flojoy(node_type="default")
def BSPLINE(
    default: OrderedPair | Matrix,
    n: int,
) -> OrderedPair | Matrix | Scalar:
    """The BSPLINE node is based on a numpy or scipy function.
    The description of that function is as follows:

            B-spline basis function of order n.

    Parameters
    ----------
    x : array_like
            a knot vector
    n : int
            The order of the spline. Must be non-negative, i.e., n >= 0

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        m=scipy.signal.bspline(
            x=default.y,
            n=n,
        )
    )

    return result
