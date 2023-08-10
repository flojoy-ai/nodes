import numpy as np
from flojoy import OrderedPair, flojoy, Scalar, Vector
from flojoy_nodes.TRANSFORMERS.ARITHMETIC.utils.arithmetic_utils import get_val
from functools import reduce


@flojoy
def MULTIPLY(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """Takes 2 input vectors, multiplies them, and returns the result"""
    initial = get_val(a)
    seq = map(lambda dc: get_val(dc), b)
    y = reduce(lambda u, v: np.multiply(u, v), seq, initial)

    match a:
        case OrderedPair():
            return OrderedPair(x=a.x, y=y)
        case Vector():
            return Vector(v=y)
        case Scalar():
            return Scalar(c=y)
