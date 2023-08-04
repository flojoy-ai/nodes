from flojoy import flojoy, OrderedPair, Vector
import numpy as np


@flojoy
def DIFFERENTIATE(default: OrderedPair | Vector) -> OrderedPair:
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

    if isinstance(default, OrderedPair):
        input_x = default.x
        input_y = default.y

        if len(input_x) != len(input_y):
            raise ValueError(f"Invalid inputs, x:{input_x} y:{input_y}")

        differentiate = np.diff(input_y) / np.diff(input_x)

        return OrderedPair(x=input_x, y=differentiate)
    else:
        input_x = np.arange((len(default.v) - 1))
        differentiate = np.zeros_like(input_x)

        for i in range(0, len(input_x)):
            differentiate[i] = default.v[i + 1] - default.v[i]

        return OrderedPair(x=input_x, y=differentiate)
