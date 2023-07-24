from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.signal


@flojoy
def GAUSS_SPLINE(
    default: OrderedPair | Matrix,
    n: int,
) -> OrderedPair | Matrix | Scalar:
    """The GAUSS_SPLINE node is based on a numpy or scipy function.
    The description of that function is as follows:

            Gaussian approximation to B-spline basis function of order n.

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
        x=default.x,
        y=scipy.signal.gauss_spline(
            x=default.y,
            n=n,
        ),
    )

    return result
