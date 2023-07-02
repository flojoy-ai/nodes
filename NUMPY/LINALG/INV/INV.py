from flojoy import DataContainer, flojoy
import numpy.linalg


@flojoy
def INV(
    default: DataContainer,
):
    """

            Compute the (multiplicative) inverse of a matrix.

            Given a square matrix `a`, return the matrix `ainv` satisfying
            ``dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])``.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : (..., M, M) array_like
            Matrix to be inverted.
    """
    return DataContainer(x=dc[0].y, y=numpy.linalg.inv(a=dc[0].y))
