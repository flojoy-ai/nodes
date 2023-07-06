import numpy as np
from flojoy import flojoy, OrderedPair
from functools import reduce


@flojoy
def DIVIDE(a: OrderedPair, b: list[OrderedPair], params: dict) -> OrderedPair:
    """Divide 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is added to an array or matrix, each element in the array or
    matrix will be increased by the constant value.
    """

    x = a.x

    y = reduce(lambda u, v: np.divide(u, v.y), b, a.y)

    return OrderedPair(x=x, y=y)
