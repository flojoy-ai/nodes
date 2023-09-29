from flojoy import flojoy, Vector, OrderedPair


@flojoy
def VECTOR_2_ORDERED_PAIR(default: Vector, y: Vector) -> OrderedPair:
    """The VECTOR_2_ORDERED_PAIR node returns the OrderedPair where x and y axes are the input nodes.

    Inputs
    ------
    default : Vector
        The input vector that will be the x axis of OrderedPair.
    y : Vector
        The input vector that will be the y axis of OrderedPair.

    Returns
    -------
    OrderedPair
        The OrderedPair that is generated from the input vectors
    """

    return OrderedPair(x=default.v, y=y.v)
