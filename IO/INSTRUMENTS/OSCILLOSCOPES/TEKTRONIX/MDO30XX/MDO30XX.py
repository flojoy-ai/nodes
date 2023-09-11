from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional


@flojoy()
def MDO30XX(default: Optional[DataContainer] = None) -> OrderedPair:
    return OrderedPair()
