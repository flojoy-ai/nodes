from flojoy import flojoy, JobResultBuilder, DataContainer, OrderedPair, NodeReference
import os
from redis import Redis
from rq.job import Job, NoSuchJobError
import traceback
from node_sdk.small_memory import SmallMemory
import numpy as np

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)


@flojoy
def REDIS_LOAD(
    default: OrderedPair, referred_node: NodeReference = ""
) -> DataContainer:
    """The REDIS_LOAD node loads data directly from REDIS.

    Parameters
    ----------
    referred_node: list of str
        The node where REDIS data will be loaded from.

    Returns
    -------
    dataframe
        The dataframe loaded from Redis. Ordered pair.
    """
    x = default.y
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

        except (Exception, NoSuchJobError):
            y = x
            print(traceback.format_exc())
            pass
        return (
            JobResultBuilder()
            .from_inputs([DataContainer(x=np.arange(0, len(y), 1), y=y)])
            .build()
        )
    else:
        return JobResultBuilder().from_inputs(default).build()
