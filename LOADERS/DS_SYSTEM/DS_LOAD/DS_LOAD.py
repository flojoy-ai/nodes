from flojoy import flojoy, JobResultBuilder, DataContainer
import os
import traceback
from flojoy.small_memory import SmallMemory
import numpy as np



@flojoy
def DS_LOAD(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The DATASTORE_LOAD node loads data directly from the Dao.

    Parameters
    ----------
    referred_node: list of str
        The node where data will be loaded from.

    Returns
    -------
    dataframe
        The dataframe loaded from Dao. Ordered pair.
    """
    referred_node = params["referred_node"]
    x = dc_inputs[0].y
    if referred_node != "":
        referred_node_key = referred_node.split("-")[0]
        try:
            y = SmallMemory().read_memory(referred_node, referred_node_key)
            print(
                "-" * 72
                + "\n" * 5
                + f"{y.size-1} iterations"
                + f" for {referred_node_key} , "
                + str([i for i in y])
                + "\n" * 5
                + "-" * 72
            )

        except Exception:
            y = x if len(dc_inputs) > 0 else [1, 3, 2]
            print(traceback.format_exc())
            pass
        return (
            JobResultBuilder()
            .from_inputs([DataContainer(x=np.arange(0, len(y), 1), y=y)])
            .build()
        )
    else:
        return JobResultBuilder().from_inputs(dc_inputs).build()
