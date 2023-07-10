import numpy as np
from flojoy import flojoy, OrderedPair


@flojoy
def ABS(default: OrderedPair) -> OrderedPair:
    """Returns abolute value"""
    return OrderedPair(x=default.y, y=np.abs(default.y))
