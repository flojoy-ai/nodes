import numpy as np
from flojoy import flojoy, Matrix


@flojoy
def MATMUL(a: Matrix, b: Matrix) -> Matrix:
    """Takes 2 input matrices, multiplies them, and returns the result"""
    return Matrix(m=np.matmul(a, b))
