import numpy as np
from flojoy import OrderedPair, flojoy, DefaultParams #type:ignore

@flojoy(node_type='ARITHMETIC')
def MULTIPLY(a: OrderedPair, b: OrderedPair, default_params:DefaultParams) -> OrderedPair:
    """Takes 2 input vectors, multiplies them, and returns the result"""
    x = a.x
    u = a.y
    v = b.y
    y = np.multiply(u, v)
    return OrderedPair(x=x, y=y)