import time
from typing import Any, Optional
from flojoy import JobResultBuilder, flojoy, DefaultParams, DataContainer


@flojoy(inject_node_metadata=True)
def TIME_DELAY(
    default_params: DefaultParams,
    default: Optional[DataContainer] = None,
    duration: float = 1.0,
) -> Any:
    time.sleep(duration)
    return JobResultBuilder().from_inputs([default]).build()