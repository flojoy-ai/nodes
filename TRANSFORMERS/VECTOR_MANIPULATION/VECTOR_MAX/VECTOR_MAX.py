import numpy as np
from flojoy import flojoy, Vector, Scalar


@flojoy
def VECTOR_MAX(default: Vector) -> Scalar:
    """The VECTOR_MAX node returns the maximum value from the Vector

    Inputs
    ------
    v : Vector
        The input vector to use max peration

    Returns
    -------
    Scalar
        The maximum value found from the input vector
    """

    return Scalar(c=np.max(default.v))
