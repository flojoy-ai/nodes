import numpy as np
from flojoy import flojoy, OrderedPair


@flojoy
def ADD(
    a: OrderedPair,
    b: OrderedPair,
) -> OrderedPair:
    """Add 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is added to an array or matrix, each element in the array or
    matrix will be increased by the constant value. If 2 arrays or matrices of different
    sizes are added, the output will be the size of the larger array or matrix with
    only the overlapping elements changed.
    """
    x = a.x
    u = a.y
    v = b.y
    y = np.add(u, v)
    return OrderedPair(x=x, y=y)
