from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def MATRIX_POWER(
    default: OrderedPair | Matrix,
    n: int,
) -> OrderedPair | Matrix | Scalar:
    """The MATRIX_POWER node is based on a numpy or scipy function.
    The description of that function is as follows:


            Raise a square matrix to the (integer) power `n`.

            For positive integers `n`, the power is computed by repeated matrix
            squarings and matrix multiplications. If ``n == 0``, the identity matrix
            of the same shape as M is returned. If ``n < 0``, the inverse
            is computed and then raised to the ``abs(n)``.

    .. note:: Stacks of object matrices are not currently supported.

    Parameters
    ----------
    a : (..., M, M) array_like
            Matrix to be "powered".
    n : int
            The exponent can be any integer or long integer, positive,
            negative, or zero.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.matrix_power(
        a=default.m,
        n=n,
    )

    if isinstance(result, np.ndarray):
        result = Matrix(m=result)
    elif isinstance(result, np.float64):
        result = Scalar(c=result)

    return result
