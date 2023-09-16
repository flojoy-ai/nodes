import numpy as np
from flojoy import flojoy, Vector


@flojoy
def SHUFFLE_VECTOR(
    default: Vector,
) -> Vector:
    """The SHUFFLE_VECTOR node returns a vector that is randomly shuffled

    Inputs
    ------
    default : Vector
        The input vector

    Returns
    -------
    Vector
        Shuffled input vector
    """

    shuffledVector = np.random.permutation(default.v)

    return Vector(v=shuffledVector)
