from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import numpy.linalg


@flojoy(node_type="default")
def EIG(
    default: OrderedPair | Matrix,
) -> OrderedPair | Matrix | Scalar:
    """The EIG node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the eigenvalues and right eigenvectors of a square array.

    Parameters
    ----------
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

    if type(result) == np.ndarray:
        result = Matrix(m=result)

    elif type(result) == np.float64:
        result = Scalar(c=result)

    return result
