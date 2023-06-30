import numpy as np
from flojoy import flojoy, OrderedPair, DefaultParams #type:ignore


@flojoy(node_type="SIMULATION")
def CONSTANT(
    default: OrderedPair, default_params: DefaultParams, constant: float = 3.0
) -> OrderedPair:
    """Generates a single x-y vector of numeric (floating point) constants"""
    x = default.y
    y = np.full(len(x), constant)
    return OrderedPair(x=x, y=y)
