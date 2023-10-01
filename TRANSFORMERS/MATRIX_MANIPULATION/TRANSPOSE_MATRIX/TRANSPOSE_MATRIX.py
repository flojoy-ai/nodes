from numpy import transpose
from flojoy import flojoy, Matrix
from typing import Optional, Union, List, Tuple


@flojoy
def TRANSPOSE_MATRIX(default: Matrix, axis: Optional[Union[List[int], Tuple[int, int]]] ) -> Matrix:
    """The TRANSPOSE_MATRIX node takes an input matrix and transpose it along the chosen axis.

    Inputs
    ------
    a : Matrix
        The input matrix to be transposed

    Parameters
    ----------
    axis : int
        Axis along which it is transposed. It takes a list of int where the length of a list is the
        number of axis in an input matrix. It will return the list where the it transpose the
        matrix based on the ith index of the list.

    Returns
    -------
    Matrix
        The matrix result from transposing.
    """
    if len(axis) > len(default.m):
        raise AssertionError("Invalid axis")
    
    return Matrix(m=transpose(default.m, axis))
