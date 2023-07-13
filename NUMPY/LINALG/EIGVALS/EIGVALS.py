from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type="default")
def EIGVALS(
    default: OrderedPair,
) -> OrderedPair:
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
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=numpy.linalg.eigvals(
            a=default.y,
        ),
    )
    return result
