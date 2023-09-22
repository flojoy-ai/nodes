from flojoy import flojoy, OrderedPair


@flojoy
def ORDERED_PAIR_XY_INVERT(
    default: OrderedPair,
) -> OrderedPair:
    """The ORDERED_PAIR_XY_INVERT node returns the OrderedPair where the axes are inverted.

    Inputs
    ------
    default : OrderedPair
        The input OrderedPair that we would like to invert the axes.

    Returns
    -------
    OrderedPair
        The OrderedPair that is inverted.
    """

    return OrderedPair(x=default.y, y=default.x)
