from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional


@flojoy()
def RPI2040(default: Optional[DataContainer] = None) -> OrderedPair:
    return OrderedPair()
