import numpy as np
from flojoy import flojoy, Vector, Scalar


@flojoy
def VECTOR_LENGTH(default: Vector) -> Scalar:
    """The VECTOR_LENGTH node returns the length of the input.

    Inputs
    ------
    v : vector
        The input vector to find the length of.

    Returns
    -------
    Scalar
        The length of the input vector.
    """

    return Scalar(c=len(default.v))
