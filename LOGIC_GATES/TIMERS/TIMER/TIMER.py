from flojoy import flojoy, DataContainer
from flojoy.job_result_builder import JobResultBuilder
import time
from typing import Any, Optional, cast

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
    remaining_time = sleep_time
    start_time = time.time()

    result = cast(
        DataContainer,
        JobResultBuilder().from_inputs([default] if default else []).build(),
    )

    remaining_time = sleep_time - (time.time() - start_time)
    time.sleep(remaining_time if remaining_time > 0 else 0)

    return result
