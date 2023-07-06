import numpy as np
from flojoy import flojoy, Matrix, DefaultParams


@flojoy
def MATRIX(params: DefaultParams) -> Matrix:
    """
    The MATRIX node takes two arguments, row and col, as input.
    Based on these inputs, it generates a random matrix where the
    integers inside the matrix are in between 0 and 19

    Parameters
    ----------
    row
        number of rows
    column
        number of columns
    Return
    ------
    matrix
        randomly generated matrix
    """

    np.random.seed()
    mat = np.random.randint(20, size=(params["row"], params["column"]))

    return Matrix(m=mat)
