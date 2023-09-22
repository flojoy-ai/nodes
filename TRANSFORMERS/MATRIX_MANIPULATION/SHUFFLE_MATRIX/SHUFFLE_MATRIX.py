from numpy.random import shuffle
from numpy import apply_along_axis
from flojoy import flojoy, Matrix


def shuffle_row(row):
    shuffle(row)
    return row

@flojoy
def SHUFFLE_MATRIX(
    default: Matrix,
    axis: int = 0,
) -> Matrix:
    """The SHUFFLE_MATRIX node returns a matrix that is randomly shuffled by the first axis

    Inputs
    ------
    default : Matrix
        The input Matrix

    Parameters
    ----------
    axis : int
        Axis along which to sort. Default is -1, which means sort along the last axis.

    Returns
    -------
    Matrix
        Shuffled input Matrix
    """

    shuffledVector = apply_along_axis(shuffle_row, axis, default.m)

    return Matrix(m=shuffledVector)
