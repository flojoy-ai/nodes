from flojoy import flojoy, DataContainer, Vector
from typing import Optional
import numpy as np


@flojoy
def RAND_VEC(default: Optional[DataContainer], size: int,
             max: float) -> Vector:
    return Vector(v=np.random.rand(size) * max)
