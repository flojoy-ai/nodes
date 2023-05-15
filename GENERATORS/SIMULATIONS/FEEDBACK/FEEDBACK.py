from flojoy import flojoy, DataContainer, get_job_result
from rq.job import NoSuchJobError
import traceback


@flojoy
def FEEDBACK(dc_inputs, params):
    referred_node = params["referred_node"]

    try:
        result = get_job_result(referred_node)
        return result
    except (Exception, NoSuchJobError) as e:
        x = dc_inputs[0].x
        y = dc_inputs[0].y
        print("Job not found: ", e, traceback.format_exc())
        return DataContainer(x=x, y=y)
