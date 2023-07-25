from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.signal


@flojoy(node_type="default")
def CUBIC(
    default: OrderedPair | Matrix,
) -> OrderedPair | Matrix | Scalar:
    """The CUBIC node is based on a numpy or scipy function.
    The description of that function is as follows:

            A cubic B-spline.

            This is a special case of `bspline`, and equivalent to ``bspline(x, 3)``.

    Parameters
    ----------
    x : array_like
            a knot vector

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = scipy.signal.cubic(
        x=default.y,
    )

    if isinstance(result, np.ndarray):
        result = OrderedPair(x=default.x, y=result)
    elif isinstance(result, np.float64 | float | np.int64 | int):
        result = Scalar(c=float(result))

    return result
