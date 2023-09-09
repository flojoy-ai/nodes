from flojoy import flojoy, Vector, OrderedPair


@flojoy
def VECTOR_2_ORDERED_PAIR(
    default: Vector,
    y: Vector
) -> OrderedPair:
    """The VECTOR_INDEXING node returns the value of the Vector at the
    requested index.

    Inputs
    ------
    x : Vector
        The input vector that will be the x axis of OrderedPair.
    y : Vector
        The input vector that will be the y axis of OrderedPair.

    Returns
    -------
    OrderedPair
        The ordered pair that is generated from the input vectors
    """

    return OrderedPair(x=default.v, y=y.v)
