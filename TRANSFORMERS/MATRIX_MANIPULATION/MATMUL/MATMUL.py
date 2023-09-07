import numpy as np
from flojoy import flojoy, Matrix


@flojoy
def MATMUL(a: Matrix, b: Matrix) -> Matrix:
    """The MATMUL node takes two input matrices, multiplies them, and returns the result.

    Inputs
    ------
    a : Matrix
        The input matrix to be multiplied to input b.
    b : Matrix
        The input matrix to be multiplied to input a.

    Returns
    -------
    Matrix
        The matrix result from the matrix multiplication.
    """

    return Matrix(m=np.matmul(a.m, b.m))
