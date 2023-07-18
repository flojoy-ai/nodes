from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def INV(
    default: OrderedPair | Matrix,
) -> OrderedPair | Matrix | Scalar:
    """The INV node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the (multiplicative) inverse of a matrix.

            Given a square matrix `a`, return the matrix `ainv` satisfying
            ``dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])``.

    Parameters
    ----------
    a : (..., M, M) array_like
            Matrix to be inverted.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.inv(
        a=default.m,
    )

    if type(result) == np.ndarray:
        result = Matrix(m=result)
    elif type(result) == np.float64:
        result = Scalar(c=result)

    return result
