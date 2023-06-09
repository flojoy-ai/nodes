import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def MATRIX(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
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

    mat = np.random.randint(20, size=(params["row"], params["col"]))
    return DataContainer(type="matrix", m=mat) 
