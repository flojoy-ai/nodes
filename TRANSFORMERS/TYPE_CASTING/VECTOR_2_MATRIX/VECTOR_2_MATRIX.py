from numpy import reshape
from flojoy import flojoy, Vector, Matrix

@flojoy
def VECTOR_2_MATRIX(default: Vector, row: int, col: int ) -> Matrix:
    """The VECTOR_2_MATRIX node takes an input matrix and transpose it along the chosen axis.

    Inputs
    ------
    default: Vector
        The input vector that will be transformed into matrix.

    Parameters
    ----------
    row: int
        number of rows for the new matrix
    col: int
        number of columns for the new matrix
    Returns
    -------
    Matrix
        The matrix that is generated from the given vector and the parameters.
    """
    if row > len(default.v):
        raise AssertionError("Invalid parameter")
    elif col * row > len(default.v):
        raise AssertionError("Invalid parameter")
    
    return Matrix(m=default.v.reshape(row,col))
    
    

