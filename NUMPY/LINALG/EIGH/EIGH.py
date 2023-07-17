from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def EIGH(
    default: OrderedPair | Matrix,
    UPLO: str = "L",
    select_return: Literal["w", "v"] = "w",
) -> OrderedPair | Matrix | Scalar:
    """The EIGH node is based on a numpy or scipy function.
    The description of that function is as follows:


            Return the eigenvalues and eigenvectors of a complex Hermitian
            (conjugate symmetric) or a real symmetric matrix.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.eigh(
        a=default.m,
        UPLO=UPLO,
    )

    if type(result) == namedtuple:
        result = result._asdict()
        result = result[select_return]

    if type(result) == np.ndarray:
        result = Matrix(m=result)
    elif type(result) == np.float64:
        result = Scalar(c=result)

    return result
