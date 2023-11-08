from numpy import stack
from flojoy import flojoy, Vector


@flojoy
def INTERLEAVE_VECTOR(
    default: Vector,
    a: list[Vector],
) -> Vector:
    """The INTERLEAVE_VECTOR node combines multiple vectors into a single vector type by interleaving their elements.

    Inputs
    ------
    default : Vector
        The input vector.

    Returns
    -------
    Vector
        The decimated vector.
    """
    
    interleavedVectors = [default.v]

    for i in range(len(a)):
        interleavedVectors = interleavedVectors + [a[i].v]

    interleavedVector = stack(interleavedVectors)
    interleavedVector = interleavedVector.T.flatten()

    return Vector(v=interleavedVector)
