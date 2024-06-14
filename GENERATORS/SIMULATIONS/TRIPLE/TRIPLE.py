from flojoy import OrderedTriple, flojoy, DataContainer, Vector
from typing import Optional
import numpy as np


@flojoy
def TRIPLE(default: Optional[DataContainer] = None) -> OrderedTriple:
    return OrderedTriple(
        x=np.array([0]),
        y=np.array([0]),
        z=np.array([0]),
    )
