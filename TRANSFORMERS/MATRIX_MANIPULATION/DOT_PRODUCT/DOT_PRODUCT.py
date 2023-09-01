import numpy as np
from flojoy import flojoy, Matrix


@flojoy
def DOT_PRODUCT(a: Matrix, b: Matrix) -> Matrix:
    """The DOT_PRODUCT node takes two input matrices, multiplies them
    (by dot product), and returns the result.

    When multiplying a scalar use the MULTIPLY node.

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
