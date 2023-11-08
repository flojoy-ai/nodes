from numpy import sort
from flojoy import flojoy, Matrix


@flojoy
def SORT_MATRIX(a: Matrix, axis: int = -1) -> Matrix:
    """The SORT_MATRIX node takes an input matrix and sorts it along the chosen axis.

    Inputs
    ------
    a : Matrix
        The input matrix to be multiplied with input b.

    Parameters
    ----------
    axis : int
        The axis along which to sort.
        Default is -1, which indicates sort along the last axis.

    Returns
    -------
    Matrix
        The matrix result after sorting.
    """

    inputMatrix = a.m
    sortedMatrix = sort(inputMatrix, axis=axis)

    return Matrix(m=sortedMatrix)
