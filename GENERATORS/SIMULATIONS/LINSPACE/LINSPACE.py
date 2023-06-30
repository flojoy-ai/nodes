import numpy as np
from flojoy import flojoy, OrderedPair, DefaultParams

@flojoy
def LINSPACE(default_params:DefaultParams, start: float=10, end: float=0, step: int=1000) -> OrderedPair:
    y = np.linspace(start, end, step)
    result = OrderedPair(x=y, y=y)
    return result