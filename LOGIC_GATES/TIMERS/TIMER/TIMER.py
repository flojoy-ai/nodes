from flojoy import flojoy, DataContainer, DefaultParams, send_to_socket
from flojoy.utils import PlotlyJSONEncoder
from flojoy.job_result_builder import JobResultBuilder
import plotly.graph_objects as go
import time
import json
from typing import Optional, cast


@flojoy(inject_node_metadata=True)
def TIMER(
    default_params: DefaultParams,
    default: Optional[DataContainer] = None,
    sleep_time: float = 0,
) -> DataContainer:
    """The TIMER node sleeps for a specified number of seconds.

    Parameters
    ----------
    sleep_time: float
        number of seconds to sleep
    """
    node_id = default_params.node_id
    jobset_id = default_params.jobset_id
    remaining_time = sleep_time
    start_time = time.time()
    current_time = start_time

    result = cast(
        DataContainer,
        JobResultBuilder().from_inputs([default] if default else []).build(),
    )

    while current_time - start_time < sleep_time:
        fig = go.Figure(
            data=go.Indicator(
                mode="number",
                value=int(remaining_time),
                domain={"y": [0, 1], "x": [0, 1]},
                delta=None,
            )
        )
        send_to_socket(
            json.dumps(
                {
                    "NODE_RESULTS": {
                        "cmd": "TIMER",
                        "id": node_id,
                        "result": {"default_fig": fig, "data": result},
                    },
                    "proceed_to_next": False,
                    "jobsetId": jobset_id,
                },
                cls=PlotlyJSONEncoder,
            ),
        )
        sleep_interval = min(1, remaining_time)
        time.sleep(sleep_interval)
        remaining_time = sleep_time - (current_time - start_time)
        current_time = time.time()

    return result
