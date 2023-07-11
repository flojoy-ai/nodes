from flojoy import flojoy, NodeReference, OrderedPair
from node_sdk.small_memory import SmallMemory
import numpy as np


@flojoy
def REDIS_LOAD(default: OrderedPair, referred_node: NodeReference) -> OrderedPair:
    """The REDIS_LOAD node loads data directly from REDIS.

    Parameters
    ----------
    referred_node: str
        The node where REDIS data will be loaded from.

    Returns
    -------
    OrderedPair
    """
    x = default.y
    if referred_node.unwrap() != "":
        referred_node_key = referred_node.unwrap().split("-")[0]
        y = SmallMemory().read_memory(referred_node.unwrap(), referred_node_key)
        if y is None:
            y = x
        print(
            "-" * 72
            + "\n" * 5
            + f"{y.size-1} iterations"
            + f" for {referred_node_key} , "
            + str([i for i in y])
            + "\n" * 5
            + "-" * 72
        )
        return OrderedPair(x=np.arange(0, len(y), 1), y=y)

    else:
        return default
