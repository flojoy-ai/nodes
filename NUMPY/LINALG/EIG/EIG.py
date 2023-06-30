from flojoy import DataContainer, flojoy, DefaultParams
import numpy.linalg

@flojoy
def EIG(default: DataContainer, default_parmas: DefaultParams):
    """

            Compute the eigenvalues and right eigenvectors of a square array.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : (..., M, M) array
            Matrices for which the eigenvalues and right eigenvectors will
            be computed
    """
    return DataContainer(x=dc[0].y, y=numpy.linalg.eig(a=dc[0].y))