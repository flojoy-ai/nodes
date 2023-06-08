from flojoy import flojoy, DataContainer, JobResultBuilder
from flojoy.utils import send_to_socket, PlotlyJSONEncoder
import plotly.graph_objects as go
import time
import json


@flojoy
def TIMER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The TIMER node sleeps for a specified number of seconds.

    Parameters
    ----------
    sleep_time: int
        number of seconds to sleep
    """
    seconds: int = params["sleep_time"]
    node_id = params["node_id"]
    jobset_id = params["jobset_id"]
    r_time = seconds
    start_time = time.time()
    current_time = start_time

    result_dc: DataContainer = JobResultBuilder().from_inputs(dc_inputs).build()

    while current_time - start_time < seconds:
        fig = go.Figure(
            data=go.Indicator(
                mode="number",
                value=r_time,
                domain={"y": [0, 1], "x": [0, 1]},
                delta=None,
            )
        )
        r_time -= 1
        send_to_socket(
            json.dumps(
                {
                    "NODE_RESULTS": {
                        "cmd": "TIMER",
                        "id": node_id,
                        "result": {"default_fig": fig, "data": result_dc},
                    },
                    "jobsetId": jobset_id,
                },
                cls=PlotlyJSONEncoder,
            ),
        )
        time.sleep(1)
        current_time = time.time()

    return result_dc
