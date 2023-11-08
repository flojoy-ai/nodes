from numpy.random import permutation
from flojoy import flojoy, Vector
from typing import TypedDict
from sklearn.model_selection import train_test_split


class resultSplit(TypedDict):
    vector1: Vector
    vector2: Vector


@flojoy
def SPLIT_VECTOR(
    default: Vector,
    index: int = 0,
) -> resultSplit:
    """The SPLIT_VECTOR node returns a vector that is split by a given index.

    Inputs
    ------
    default : Vector
        The input vector.

    Parameters
    ----------
    index : int
        The index by which the vector should be split.

    Returns
    -------
    Vector
        The splited input vector.
    """
    
    if index > len(default.v) - 1:
        raise ValueError(f"Given index is larger than the input vector, index: {index}")

    return resultSplit(
        vector1=Vector(default.v[:index]), vector2=Vector(default.v[index:])
    )
