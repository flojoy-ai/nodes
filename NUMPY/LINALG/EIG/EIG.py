from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def EIG(
    default: Matrix,
    select_return: Literal["w", "v"] = "w",
) -> Matrix | Scalar:
    """The EIG node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the eigenvalues and right eigenvectors of a square array.

    Parameters
    ----------
    select_return : This function has returns multiple Objects:
            ['w', 'v']. Select the desired one to return.
            See the respective function docs for descriptors.
    a : (..., M, M) array
            Matrices for which the eigenvalues and right eigenvectors will
            be computed

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.eig(
        a=default.m,
    )

    if isinstance(result, namedtuple):
        result = result._asdict()
        result = result[select_return]

    if isinstance(result, np.ndarray):
        result = Matrix(m=result)
    elif isinstance(result, np.float64):
        result = Scalar(c=result)

    return result
