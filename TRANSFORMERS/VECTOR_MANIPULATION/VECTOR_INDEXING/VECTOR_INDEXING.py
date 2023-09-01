import numpy as np
from flojoy import flojoy, Vector, Scalar


@flojoy
def VECTOR_INDEXING(
    default: Vector,
    index: int = 0,
) -> Scalar:
    """The VECTOR_LENGTH node returns the length of the input

    Inputs
    ------
    v : Vector
        The input vector to find the length of.

    Parameters
    ----------
    index : int
        The index of the vector to return.

    Returns
    -------
    Scalar
        The scalar index of the input vector.
    """

    return Scalar(c=default.v[index])
