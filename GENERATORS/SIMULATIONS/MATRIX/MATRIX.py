import numpy as np
from flojoy import flojoy, Matrix


@flojoy
def MATRIX(row: int = 2, column: int = 2) -> Matrix:
    """The MATRIX node takes two arguments, 'row' and 'col', as input.

    Based on these inputs, it generates a random matrix where the integers inside the matrix are between 0 and 19.

    Parameters
    ----------
    row : int
        number of rows
    column : int
        number of columns

    Returns
    -------
    matrix
        randomly generated matrix
    """

    np.random.seed()
    mat = np.random.randint(20, size=(row, column))

    return Matrix(m=mat)
