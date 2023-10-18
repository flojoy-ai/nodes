from flojoy import flojoy, DataContainer
from flojoy.job_result_builder import JobResultBuilder
import time
from typing import Optional, cast


@flojoy()
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

    remaining_time = sleep_time
    start_time = time.time()
    current_time = start_time

    result = cast(
        DataContainer,
        JobResultBuilder().from_inputs([default] if default else []).build(),
    )

    while current_time - start_time < sleep_time:
        sleep_interval = min(1, remaining_time)
        time.sleep(sleep_interval)
        remaining_time = sleep_time - (current_time - start_time)
        current_time = time.time()

    return result
