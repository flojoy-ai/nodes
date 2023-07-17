from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.signal


@flojoy(node_type="default")
def QUADRATIC(
    default: OrderedPair | Matrix,
) -> OrderedPair | Matrix | Scalar:
    """The QUADRATIC node is based on a numpy or scipy function.
    The description of that function is as follows:

            A quadratic B-spline.

            This is a special case of `bspline`, and equivalent to ``bspline(x, 2)``.

    Parameters
    ----------
    x : array_like
            a knot vector

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        x=default.x,
        y=scipy.signal.quadratic(
            x=default.y,
        ),
    )

    return result
