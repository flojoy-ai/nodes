import numpy as np
from flojoy import OrderedPair, flojoy, Scalar, Vector
from nodes.TRANSFORMERS.ARITHMETIC.utils.arithmetic_utils import get_val
from functools import reduce


@flojoy
def MULTIPLY(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """
    The MULTIPLY node takes two input vectors, multiplies them, and returns the result.

    Inputs
    ------
    a : OrderedPair|Scalar|Vector
        Input a that we will multiply to input b.
    b : OrderedPair|Scalar|Vector
        Input b that we will multiply to input a.
    
    Returns
    -------
    OrderedPair|Scalar|Vector
        OrderedPair if...
        x : the x-axis of the a input.
        y : the result of the multiplication of input a and input b.
    
        Scalar if...
        c : the result of the multiplication of input a and input b.
    
        Vector if...
        v : the result of the multiplication of input a and input b.
    """

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
