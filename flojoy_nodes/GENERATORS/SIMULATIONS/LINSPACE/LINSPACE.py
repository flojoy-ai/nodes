import numpy as np
from flojoy import flojoy, Vector


@flojoy(node_type="default")
def LINSPACE(start: float = 10, end: float = 0, step: int = 1000) -> Vector:
    """The LINSPACE node generates data spaced evenly between two points.
    It uses the numpy function linspace. It is useful for generating an x axis
    for ordered pair type data.

    Parameters
    ----------
    start: float
        The start point of the data
    end: float
        The end point of the data.
    step: float
        The number of points in the vector.

    Returns
    -------
    Vector
        The vector between start and end with step number of points.
    """
    v = np.linspace(start, end, step)
    return Vector(v=v)
