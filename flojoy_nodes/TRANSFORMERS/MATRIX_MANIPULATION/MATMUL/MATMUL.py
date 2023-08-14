import numpy as np
from flojoy import flojoy, Matrix


@flojoy
def MATMUL(a: Matrix, b: Matrix) -> Matrix:
    """The MATMUL node takes two input matrices, multiplies them, and returns the result."""

    return Matrix(m=np.matmul(a.m, b.m))
