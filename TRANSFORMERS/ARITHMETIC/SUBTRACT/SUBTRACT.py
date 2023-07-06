import numpy as np
from flojoy import flojoy, OrderedPair


@flojoy
def SUBTRACT(a: OrderedPair, b: OrderedPair) -> OrderedPair:
    """Subtract 2 input vectors and return the result"""

    x = a.x
    u = a.y
    v = b.y

    y = np.subtract(u, v)

    return OrderedPair(x=x, y=y)
