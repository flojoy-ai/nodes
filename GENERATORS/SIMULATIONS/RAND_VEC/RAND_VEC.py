from flojoy import flojoy, DataContainer, Vector
from typing import Optional
import numpy as np


@flojoy
def RAND_VEC(
    default: Optional[DataContainer] = None, size: int = 3, max: float = 1
) -> Vector:
    return Vector(v=np.random.rand(size) * max)
