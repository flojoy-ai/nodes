from flojoy import flojoy, DataContainer, DefaultParams
from flojoy.utils import PlotlyJSONEncoder
from flojoy.job_result_builder import JobResultBuilder
import plotly.graph_objects as go
import time
import json
from typing import Optional, cast


@flojoy
def TIMER(
    default: Optional[DataContainer] = None,
    sleep_time: float = 0,
) -> DataContainer:
    """The TIMER node sleeps for a specified number of seconds.

    Parameters
    ----------
    sleep_time : float
        number of seconds to sleep
    """

    time.sleep(sleep_time)
    result = cast(
        DataContainer,
        JobResultBuilder().from_inputs([default] if default else []).build(),
    )

    return result
