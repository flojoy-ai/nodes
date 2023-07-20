import numpy as np
from flojoy import flojoy, Vector


@flojoy(node_type="default")
def LINSPACE(start: float = 10, end: float = 0, step: int = 1000) -> Vector:
    v = np.linspace(start, end, step)
    return Vector(v=v)
