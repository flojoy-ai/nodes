from flojoy import DataContainer, flojoy
import numpy.linalg


@flojoy
def EIGVALS(dc, params):
    """

            Compute the eigenvalues of a general matrix.

    Main difference between `eigvals` and `eig`: the eigenvectors aren't
            returned.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : (..., M, M) array_like
            A complex- or real-valued matrix whose eigenvalues will be computed.
    """
    return DataContainer(
        x=dc[0].y,
        y=numpy.linalg.eigvals(
            a=dc[0].y,
        ),
    )
