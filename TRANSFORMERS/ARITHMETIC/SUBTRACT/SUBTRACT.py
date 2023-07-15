import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from nodes.TRANSFORMERS.ARITHMETIC.utils.arithmetic_utils import get_param_keys
from functools import reduce


@flojoy
def SUBTRACT(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """Subtract 2 input vectors and return the result"""
    initial = get_param_keys(a)
    seq = map(lambda dc: get_param_keys(dc), b)
    y = reduce(lambda u, v: np.subtract(u, v), seq, initial)

    match a:
        case OrderedPair():
            return OrderedPair(x=a.x, y=y)
        case Vector():
            return Vector(v=y)
        case Scalar():
            return Scalar(c=y)
