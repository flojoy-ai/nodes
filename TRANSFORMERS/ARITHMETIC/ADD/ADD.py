import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from nodes.TRANSFORMERS.ARITHMETIC.utils.arithmetic_utils import get_val
from functools import reduce


@flojoy
def ADD(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """
    The ADD node adds two or more numeric arrays, matrices, dataframes, or constants element-wise.

    When a constant is added to an array or matrix, each element in the array or matrix will be increased by the constant value.

    If two arrays or matrices of different sizes are added, the output will be the size of the larger array or matrix with only the overlapping elements changed.

    Inputs
    ------
    a : OrderedPair|Scalar|Vector
        Input a that we will add with input b.
    b : OrderedPair|Scalar|Vector
        Input b that we will add with input a.

    Returns
    -------
    OrderedPair|Scalar|Vector
        OrderedPair if...
        x : the x-axis of the a input.
        y : the sum of the input a and input b.

        Scalar if...
        c : the sum of the input a and input b.

        Vector if...
        v : the sum of the input a and input b.
    """

    initial = get_val(a)
    seq = map(lambda dc: get_val(dc), b)
    y = reduce(lambda u, v: np.add(u, v), seq, initial)

    match a:
        case OrderedPair():
            return OrderedPair(x=a.x, y=y)
        case Vector():
            return Vector(v=y)
        case Scalar():
            return Scalar(c=y)
