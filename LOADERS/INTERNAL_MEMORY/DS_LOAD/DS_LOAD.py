from flojoy import flojoy, NodeReference, OrderedPair, SmallMemory
import numpy as np


@flojoy
def DS_LOAD(default: OrderedPair, referred_node: NodeReference) -> OrderedPair:
    """The DS_LOAD node loads data directly from in-memory data storage.

    Parameters
    ----------
    referred_node : str
        The ID of the node to retrieve the result from.

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
