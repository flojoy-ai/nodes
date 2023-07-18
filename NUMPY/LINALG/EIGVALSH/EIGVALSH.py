from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def EIGVALSH(
    default: OrderedPair | Matrix,
    UPLO: str = "L",
) -> OrderedPair | Matrix | Scalar:
    """The EIGVALSH node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the eigenvalues of a complex Hermitian or real symmetric matrix.

    Main difference from eigh: the eigenvectors are not computed.

    Parameters
    ----------
    a : (..., M, M) array_like
            A complex- or real-valued matrix whose eigenvalues are to be
            computed.
    UPLO : {'L', 'U'}, optional
            Specifies whether the calculation is done with the lower triangular
            part of `a` ('L', default) or the upper triangular part ('U').
            Irrespective of this value only the real parts of the diagonal will
            be considered in the computation to preserve the notion of a Hermitian
            matrix. It therefore follows that the imaginary part of the diagonal
            will always be treated as zero.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.eigvalsh(
        a=default.m,
        UPLO=UPLO,
    )

    if isinstance(result, np.ndarray):
        result = Matrix(m=result)
    elif isinstance(result, np.float64):
        result = Scalar(c=result)

    return result
