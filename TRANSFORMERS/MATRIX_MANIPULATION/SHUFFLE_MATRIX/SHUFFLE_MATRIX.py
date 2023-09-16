import numpy as np
from flojoy import flojoy, Matrix

@flojoy
def SHUFFLE_MATRIX(
    default: Matrix,
) -> Matrix:
    """The SHUFFLE_MATRIX node returns a matrix that is randomly shuffled by the first axis

    Inputs
    ------
    default : Matrix
        The input Matrix

    Returns
    -------
    Matrix
        Shuffled input Matrix
    """

    shuffledVector = np.random.permutation(default.m)

    return Matrix(m=shuffledVector)