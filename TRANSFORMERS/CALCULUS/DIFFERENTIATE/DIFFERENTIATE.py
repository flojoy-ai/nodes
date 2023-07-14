from flojoy import flojoy, OrderedPair
import numpy as np


@flojoy
def DIFFERENTIATE(default: OrderedPair) -> OrderedPair:
    """
    The DIFFERENTIATE node takes two list, x and y, as input.
    It computes the derivative of the array, y with respect to x.

    Parameters
    ----------
    None

    Returns
    -------
    numpy array
        Derivative of the array
    """
    input_x = default.x
    input_y = default.y

    if len(input_x) != len(input_y):
        raise ValueError(f"Invalid inputs, x:{input_x} y:{input_y}")

    differentiate = np.diff(input_y) / np.diff(input_x)

    return OrderedPair(x=input_x, y=differentiate)
