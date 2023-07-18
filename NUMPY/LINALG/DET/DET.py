from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def DET(
    default: OrderedPair | Matrix,
) -> OrderedPair | Matrix | Scalar:
    """The DET node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the determinant of an array.

    Parameters
    ----------
    a : (..., M, M) array_like
            Input array to compute determinants for.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.det(
        a=default.m,
    )

    if type(result) == np.ndarray:
        result = Matrix(m=result)
    elif type(result) == np.float64:
        result = Scalar(c=result)

    return result
