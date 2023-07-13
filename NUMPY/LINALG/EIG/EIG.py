from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type="default")
def EIG(
    default: OrderedPair,
) -> OrderedPair:
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
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=numpy.linalg.eig(
            a=default.y,
        ),
    )
    return result
