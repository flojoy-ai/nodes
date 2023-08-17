import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from nodes.TRANSFORMERS.ARITHMETIC.utils.arithmetic_utils import get_val

def reduce(func, seq, initial):
    result = initial
    for item in seq:
        result = func(result, item)
    return result

@flojoy
def ADD(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """The ADD node adds two or more numeric arrays, matrices, dataframes, or constants element-wise.

    When a constant is added to an array or matrix, each element in the array or matrix will be increased by the constant value.

    If two arrays or matrices of different sizes are added, the output will be the size of the larger array or matrix with only the overlapping elements changed.

    Inputs
    ------
    a : OrderedPair|Scalar|Vector
        The input a use to compute the sum of a and b.
    b : OrderedPair|Scalar|Vector
        The input b use to compute the sum of a and b.

    Returns
    -------
    OrderedPair|Scalar|Vector
        OrderedPair if a is an OrderedPair.
        x: the x-axis of input a.
        y: the sum of input a and input b.

        Scalar if a is a Scalar.
        c: the sum of input a and input b.

        Vector if a is a Vector.
        v: the sum of input a and input b.
    """

    initial = get_val(a)
    seq = map(lambda dc: get_val(dc), b)
    y = reduce(lambda u, v: u+v, seq, initial)

    if isinstance(a, OrderedPair):
        return OrderedPair(x=a.x, y=y)
    elif isinstance(a, Vector):
        return Vector(v=y)
    elif isinstance(a, Scalar):
        return Scalar(c=y)

