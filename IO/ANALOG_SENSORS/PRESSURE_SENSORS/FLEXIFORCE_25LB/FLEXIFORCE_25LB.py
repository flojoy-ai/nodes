from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional


@flojoy(deps={"pyserial": "3.5"})
def FLEXIFORCE_25LB(default: Optional[DataContainer] = None) -> OrderedPair:
    return OrderedPair()
