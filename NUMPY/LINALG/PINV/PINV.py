from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def PINV(
    default: OrderedPair | Matrix,
    rcond: float = 1e-15,
    hermitian: bool = False,
) -> OrderedPair | Matrix | Scalar:
    """The PINV node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the (Moore-Penrose) pseudo-inverse of a matrix.

            Calculate the generalized inverse of a matrix using its
            singular-value decomposition (SVD) and including all
            *large* singular values.

    .. versionchanged:: 1.14
            Can now operate on stacks of matrices

    Parameters
    ----------
    a : (..., M, N) array_like
            Matrix or stack of matrices to be pseudo-inverted.
    rcond : (...) array_like of float
            Cutoff for small singular values.
            Singular values less than or equal to
            ``rcond * largest_singular_value`` are set to zero.
            Broadcasts against the stack of matrices.
    hermitian : bool, optional
            If True, `a` is assumed to be Hermitian (symmetric if real-valued),
            enabling a more efficient method for finding singular values.
            Defaults to False.

    .. versionadded:: 1.17.0

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.pinv(
        a=default.m,
        rcond=rcond,
        hermitian=hermitian,
    )

    if type(result) == np.ndarray:
        result = Matrix(m=result)
    elif type(result) == np.float64:
        result = Scalar(c=result)

    return result
