from flojoy import flojoy, DataContainer, get_job_result
from rq.job import NoSuchJobError
import traceback


@flojoy
def FEEDBACK(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    The FEEDBACK node takes one reference node as  a parameter and returns the data from this node's most recent output.

    Parameters
    ----------
    referred_node

    Return
    ------
    Data container from referred_node
    """
    referred_node = params["referred_node"]

    try:
        result = get_job_result(referred_node)
        return result
    except (Exception, NoSuchJobError) as e:
        x = dc_inputs[0].x
        y = dc_inputs[0].y
        print("Job not found: ", e, traceback.format_exc())
        return DataContainer(x=x, y=y)
