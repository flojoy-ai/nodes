from numpy import reshape
from flojoy import flojoy, Vector, Matrix


@flojoy
def VECTOR_2_MATRIX(default: Vector, row: int, col: int) -> Matrix:
    """The VECTOR_2_MATRIX node takes a vector and transform it into matrix data type where
    the shape is chosen by row and col parameters.

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
    try:
        matrix = default.v.reshape((row, col))
        return Matrix(m=matrix)
    except Exception as e:
        print(e)
