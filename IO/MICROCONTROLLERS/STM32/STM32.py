from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional


@flojoy()
def STM32(default: Optional[DataContainer] = None) -> OrderedPair:
    return OrderedPair()
