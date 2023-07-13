from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type="default")
def INV(
    default: OrderedPair,
) -> OrderedPair:
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
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=numpy.linalg.inv(
            a=default.y,
        ),
    )
    return result
