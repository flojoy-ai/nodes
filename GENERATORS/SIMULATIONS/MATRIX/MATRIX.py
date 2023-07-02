import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def MATRIX(default: DataContainer, row: int = 2, column: int = 2) -> DataContainer:
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
    return DataContainer(type="matrix", m=mat)
