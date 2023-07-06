import numpy as np
from flojoy import flojoy, DataContainer, OrderedPair, Matrix


@flojoy
def MATMUL(matrix_1: OrderedPair, matrix_2: OrderedPair) -> DataContainer:
    """Takes 2 input matrices, multiplies them, and returns the result"""
    a = matrix_1.y
    b = matrix_2.y

    return Matrix(m=np.matmul(a, b))
