from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional


@flojoy()
def SCPI(default: Optional[DataContainer] = None) -> OrderedPair:
    return OrderedPair()
