from flojoy import flojoy, OrderedPair, DefaultParams
import numpy as np


@flojoy
def DIFFERENTIATE(default : OrderedPair) -> OrderedPair:
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
    
    differentiate = np.diff(input_y) / np.diff(input_x)
    return OrderedPair(x=input_x, y=differentiate)
