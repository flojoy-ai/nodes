from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional


@flojoy()
def ESP32(default: Optional[DataContainer] = None) -> OrderedPair:
    return OrderedPair()
