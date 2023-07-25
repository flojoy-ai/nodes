from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.stats


@flojoy
def TRIM1(
    default: OrderedPair | Matrix,
    proportiontocut: float = 0.1,
    tail: str = "right",
    axis: int = 0,
) -> OrderedPair | Matrix | Scalar:
    """The TRIM1 node is based on a numpy or scipy function.
    The description of that function is as follows:

            Slice off a proportion from ONE end of the passed array distribution.

            If `proportiontocut` = 0.1, slices off 'leftmost' or 'rightmost'
            10% of scores. The lowest or highest values are trimmed (depending on
            the tail).
            Slice off less if proportion results in a non-integer slice index
            (i.e. conservatively slices off `proportiontocut` ).

    Parameters
    ----------
    a : array_like
            Input array.
    proportiontocut : float
            Fraction to cut off of 'left' or 'right' of distribution.
    tail : {'left', 'right'}, optional
            Defaults to 'right'.
    axis : int or None, optional
            Axis along which to trim data. Default is 0. If None, compute over
            the whole array `a`.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = scipy.stats.trim1(
        a=default.y,
        proportiontocut=proportiontocut,
        tail=tail,
        axis=axis,
    )

    if isinstance(result, np.ndarray):
        result = OrderedPair(x=default.x, y=result)
    elif isinstance(result, np.float64 | float | np.int64 | int):
        result = Scalar(c=float(result))

    return result
