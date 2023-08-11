import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from nodes.TRANSFORMERS.ARITHMETIC.utils.arithmetic_utils import get_val
from functools import reduce


@flojoy
def SUBTRACT(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """
    The SUBTRACT node subtracts two input vectors and returns the result.

    Inputs
    ------
    a : OrderedPair|Scalar|Vector
        Input from which we will subtract input b.
    b : OrderedPair|Scalar|Vector
        Input we will subtract from input a.
    
    Returns
    -------
    OrderedPair|Scalar|Vector
        OrderedPair if...
        x : the x-axis of the input a.
        y : the result of the subtraction of input b to input a.
    
        Scalar if...
        c : the result of the subtraction of input b to input a.
    
        Vector if...
        v : the result of the subtraction of input b to input a.
    """

    initial = get_val(a)
    seq = map(lambda dc: get_val(dc), b)
    y = reduce(lambda u, v: np.subtract(u, v), seq, initial)

    match a:
        case OrderedPair():
            return OrderedPair(x=a.x, y=y)
        case Vector():
            return Vector(v=y)
        case Scalar():
            return Scalar(c=y)
