from flojoy import flojoy, Vector, OrderedPair
from typing import TypedDict


class resultSplit(TypedDict):
    x: Vector
    y: Vector


@flojoy
def ORDERED_PAIR_2_VECTOR(default: OrderedPair) -> resultSplit:
    """The ORDERED_PAIR_2_VECTOR return the split components of an ordered pair as Vectors.

    Inputs
    ------
    default : OrderedPair
        The input OrderedPair.

    Returns
    -------
    x : Vector
        Vector from input x
    y : Vector
        Vector from input y
    """

    return resultSplit(x=Vector(v=default.x), y=Vector(v=default.y))
