from flojoy import (
    flojoy,
    Scalar,
    OrderedPair,
    SmallMemory,
    NodeReference,
    DefaultParams,
)
import os
from rq.job import Job, NoSuchJobError
import traceback
import numpy as np
from typing import Optional


memory_key = "LOOP_INDEX"


@flojoy(node_type="default", inject_node_metadata=True)
def LOOP_INDEX(
    referred_node: NodeReference,
    default_params: DefaultParams,
    default: Optional[OrderedPair | Scalar] = None,
) -> Scalar:
    """The LOOP_INDEX node loads the loop index from the LOOP node.
    A loop index in Flojoy starts at 1 and increases by 1 for each loop.

    Parameters
    ----------
    referred_node: list of str
        The LOOP node to track the loop index from.

    Returns
    -------
    Scalar
        The loop index in Scalar form.
    """

    node_id = default_params.node_id

    if referred_node.unwrap() != "":
        try:
            y = SmallMemory().read_memory(referred_node.unwrap(), "loop-info")
            if y is None:
                y = SmallMemory().read_memory(node_id, memory_key)
                if y is None:
                    y = np.ones(1)
                SmallMemory().write_to_memory(node_id, memory_key, y + 1)
                c = y[0]
            else:
                c = y["current_iteration"]
        except (Exception, NoSuchJobError):
            print(traceback.format_exc())

        return Scalar(c=float(c))

    else:
        raise ValueError("LOOP_INDEX: please select a node.")
