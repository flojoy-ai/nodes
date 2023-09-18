from flojoy import flojoy, Vector


@flojoy
def DECREMENT_ELEMENT(default: Vector, value: int) -> Vector:
    """The DECREMENT_ELEMENT node decrements the elements by the specified value from the Vector

    Inputs
    ------
    v : Vector
        The input vector to decrement values from

    Parameters
    ----------
    value: int
        the amount to decrement for each element

    Returns
    -------
    Vector
        The new vector with elements decremented from the input vector
    """
    v = default.v - value
    return Vector(v=v)
