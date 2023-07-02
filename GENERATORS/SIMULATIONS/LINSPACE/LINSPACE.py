import numpy as np
from flojoy import flojoy, OrderedPair, ParameterTypes


@flojoy(node_type="default")
def LINSPACE(
    start: ParameterTypes.FLOAT = 10,
    end: ParameterTypes.FLOAT = 0,
    step: ParameterTypes.INT = 1000,
) -> OrderedPair:
    y = np.linspace(start, end, step)
    result = OrderedPair(x=y, y=y)
    return result
