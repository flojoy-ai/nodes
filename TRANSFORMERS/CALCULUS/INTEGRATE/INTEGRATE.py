from flojoy import flojoy, OrderedPair, Vector
import numpy as np


def trapz(x, y):
    m = [0] * len(x)
    trapezium = (1 / 2) * (x[1] - x[0]) * (y[1] + y[0])
    m[1] = trapezium

    for i in range(2, len(x)):
        trapezium = (1 / 2) * (x[i] - x[i - 1]) * (y[i] + y[i - 1])
        m[i] = m[i - 1] + trapezium

    return m


@flojoy
def INTEGRATE(default: OrderedPair | Vector) -> OrderedPair:
    """
    The INTEGRATE node takes two lists as input and integrates it using the composite
    trapezoidal rule.

    Parameters
    ----------
    None

    Returns
    -------
    OrderedPair, x, y
    """
    if isinstance(default, OrderedPair):
        input_x = default.x
        input_y = default.y
    else:
        input_x = np.zeros_like(default.v)
        for i in range(0, len(default.v)):
            input_x[i] = i
        input_y = default.v

    if type(input_x) != np.ndarray:
        raise ValueError(f"Invalid type for x:{type(input_x)}")
    elif type(input_y) != np.ndarray:
        raise ValueError(f"Invalid type for y:{type(input_y)}")
    elif len(input_x) != len(input_y):
        raise ValueError(f"Invalid inputs, x:{input_x} y:{input_y}")

    integrate = trapz(input_x, input_y)

    return OrderedPair(x=input_x, y=integrate)
