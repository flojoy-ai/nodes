import numpy as np
from flojoy import flojoy, Vector

@flojoy
def REMOVE_DUPLICATES_VECTOR(
    default: Vector,
) -> Vector:
    """The REMOVE_DUPLICATES_VECTOR node returns a vector with only unique elements

    Inputs
    ------
    default : Vector
        The input vector

    Returns
    -------
    Vector
        Unique input vector
    """

    return Vector(v=np.unique(default.v))
