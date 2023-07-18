from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def EIGVALS(
    default: OrderedPair | Matrix,
) -> OrderedPair | Matrix | Scalar:
    """The EIGVALS node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the eigenvalues of a general matrix.

    Main difference between `eigvals` and `eig`: the eigenvectors aren't
            returned.

    Parameters
    ----------
    a : (..., M, M) array_like
            A complex- or real-valued matrix whose eigenvalues will be computed.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.eigvals(
        a=default.m,
    )

    if isinstance(result, np.ndarray):
        result = Matrix(m=result)
    elif isinstance(result, np.float64):
        result = Scalar(c=result)

    return result
