import numpy as np
from flojoy import flojoy, Matrix


@flojoy
def SORT_MATRIX(a: Matrix, axis: int = -1) -> Matrix:
    """The SORT_MATRIX node takes a input matrix and sort it by the axis.

    Inputs
    ------
    a : Matrix
        The input matrix to be multiplied to input b

    Parameters
    ----------
    axis : int
        Axis along which to sort. Default is -1, which means sort along the last axis.

    Returns
    -------
    Matrix
        The matrix result from the matrix multiplication.
    """
    inputMatrix = a.m
    sortedMatrix = np.sort(inputMatrix, axis=axis)

    return Matrix(m=sortedMatrix)
