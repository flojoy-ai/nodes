
from numpy import array
from flojoy import flojoy, Vector


@flojoy
def INCREMENT_ELEMENT(default: Vector, value: int) -> Vector:
    """The INCREMENT_ELEMENT node decrements the elements by the specified value from the Vector

    Inputs
    ------
    v : Vector
        The input vector to increment values from

    Parameters
    ----------
    value: int
        the amount to increment for each element

    Returns
    -------
    Vector
        The new vector with elements incremented from the input vector
    """
    v = default.v + value
    return Vector(v=v)
