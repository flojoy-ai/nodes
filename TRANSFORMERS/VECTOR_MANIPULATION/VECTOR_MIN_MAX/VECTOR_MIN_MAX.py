import numpy as np
from flojoy import flojoy, Vector, Scalar
from typing import Literal


@flojoy
def VECTOR_MIN_MAX(default: Vector, operation: Literal["min", "max"] = "max") -> Scalar:
    """The VECTOR_MIN_MAX node returns the maximum or minimum value from the Vector

    Inputs
    ------
    v : Vector
        The input vector to use min or max operation

    Parameters
    ----------
    operation: "min" | "max", default="max"
        Select whether to find the maximum or minimum element in input vector

    Returns
    -------
    Scalar
        The maximum or minimum value found based on the operation performed
    """

    match operation:
        case "min":
            c = np.min(default.v)
        case "max":
            c = np.max(default.v)
    return Scalar(c=c)
