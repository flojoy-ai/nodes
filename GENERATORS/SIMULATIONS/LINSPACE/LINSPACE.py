import numpy as np
from flojoy import flojoy, Vector


@flojoy(node_type="default")
def LINSPACE(start: float = 10, end: float = 0, step: int = 1000) -> Vector:
    """The LINSPACE node generates an array containing evenly spaced numbers over a specified interval

    Parameters
    ---------
    start: float
        the first value of the output vector, or the start of the interval
    end: float
        the last value of the output vector, or the end of the interval
    step: int
        number of samples to generate

    Returns
    -------
    Vector
        v: equally spaced samples in the interval [start, stop]

    """
    v = np.linspace(start, end, step)
    return Vector(v=v)
