import numpy as np
from flojoy import OrderedPair, flojoy, Scalar, Vector
from nodes.TRANSFORMERS.ARITHMETIC.util.arithmetic_utils import get_param_keys
from functools import reduce


@flojoy
def MULTIPLY(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """Takes 2 input vectors, multiplies them, and returns the result"""
    initial = get_param_keys(a)
    seq = map(lambda dc: get_param_keys(dc), b)
    y = reduce(lambda u, v: np.multiply(u, v), seq, initial)

    match a:
        case OrderedPair():
            return OrderedPair(x=a.x, y=y)
        case Vector():
            return Vector(v=y)
        case Scalar():
            return Scalar(c=y)
