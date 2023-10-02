import numpy as np
from flojoy import flojoy, Vector, Scalar


@flojoy
def VECTOR_MIN(default: Vector) -> Scalar:
    """The VECTOR_MIN node returns the minimum value from the Vector

    Inputs
    ------
    v : Vector
        The input vector to use min peration

    Returns
    -------
    Scalar
        The minimum value found from the input vector
    """

    return Scalar(c=np.min(default.v))
