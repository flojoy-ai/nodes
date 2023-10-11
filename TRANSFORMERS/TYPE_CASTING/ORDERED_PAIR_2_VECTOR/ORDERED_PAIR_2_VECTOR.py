from flojoy import flojoy, Vector, OrderedPair


@flojoy
def ORDERED_PAIR_2_VECTOR(default: OrderedPair) -> Vector:
    """The ORDERED_PAIR_2_VECTOR return the y component of an ordered pair as a Vector.

    Inputs
    ------
    default : OrderedPair
        The input OrderedPair.

    Returns
    -------
    Vector
        The y component of the input OrderedPair.
    """

    return Vector(v=default.y)
