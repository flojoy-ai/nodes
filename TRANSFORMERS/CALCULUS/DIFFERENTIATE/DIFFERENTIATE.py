from flojoy import flojoy, OrderedPair, Vector
import numpy as np


def diff(input_x, input_y):
    result = np.zeros_like(input_x)
    for i in range(0, len(input_x)):
        result[i] = input_y[i + 1] - input_y[i]

    return result


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
        x_axis = [0] * (len(default.v) - 1)
        input_x = np.array(x_axis)
        for i in range(0, (len(input_x))):
            input_x[i] = i

        differentiate = diff(input_x, default.v)

        return OrderedPair(x=input_x, y=differentiate)
