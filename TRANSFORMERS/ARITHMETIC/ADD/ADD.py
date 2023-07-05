import numpy as np
from flojoy import flojoy, OrderedPair
from functools import reduce


@flojoy
def ADD(a: OrderedPair, b: list[OrderedPair]) -> OrderedPair:
    """Add 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is added to an array or matrix, each element in the array or
    matrix will be increased by the constant value. If 2 arrays or matrices of different
    sizes are added, the output will be the size of the larger array or matrix with
    only the overlapping elements changed.
    """
    # TODO: Support other data types
    x = a.x

    y = reduce(lambda u, v: np.add(u, v.y), b, a.y)

    return OrderedPair(x=x, y=y)
