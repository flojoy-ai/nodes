import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from nodes.TRANSFORMERS.ARITHMETIC.utils.arithmetic_utils import get_param_keys
from functools import reduce


@flojoy
def DIVIDE(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """Divide 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is divideed to an array or matrix, each element in the array or
    matrix will be increased by the constant value.
    """
    initial = get_param_keys(a)
    seq = map(lambda dc: get_param_keys(dc), b)
    y = reduce(lambda u, v: np.divide(u, v), seq, initial)

    match a:
        case OrderedPair():
            return OrderedPair(x=a.x, y=y)
        case Vector():
            return Vector(v=y)
        case Scalar():
            return Scalar(c=y)
