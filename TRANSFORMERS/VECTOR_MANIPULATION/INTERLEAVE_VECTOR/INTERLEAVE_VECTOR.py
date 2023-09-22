import numpy as np
from flojoy import flojoy, Vector


@flojoy
def INTERLEAVE_VECTOR(
    default: Vector,
    a: list[Vector],
) -> Vector:
    """The INTERLEAVE_VECTOR node combine multiple vectors
    into a single vector type by interleaving their elements

    Inputs
    ------
    default : Vector
        The input vector

    Returns
    -------
    Vector
        Decimated vector
    """
    interleavedVectors = [default.v]

    for i in range(len(a)):
        interleavedVectors = interleavedVectors + [a[i].v]

    interleavedVector = np.stack(interleavedVectors)
    interleavedVector = interleavedVector.T.flatten()

    return Vector(v=interleavedVector)
