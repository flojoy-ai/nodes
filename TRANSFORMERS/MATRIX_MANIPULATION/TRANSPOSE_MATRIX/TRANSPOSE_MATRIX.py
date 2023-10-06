from numpy import transpose
from flojoy import flojoy, Matrix


@flojoy
def TRANSPOSE_MATRIX(default: Matrix) -> Matrix:
    """The TRANSPOSE_MATRIX node takes an input matrix and transpose it along the chosen axis.

    Inputs
    ------
    a : Matrix
        The input matrix to be transposed

    Returns
    -------
    Matrix
        The matrix result from transposing.
    """
    
    return Matrix(m=transpose(default.m, (1,0)))
