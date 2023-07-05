from flojoy import flojoy, OrderedPair
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
def INTEGRATE(default: OrderedPair, params: dict) -> OrderedPair:
    """
    The INTEGRATE node takes two lists as input and integrates it using the composite
    trapezoidal rule.

    Parameters
    ----------
    None

    Returns
    -------
    DataContainer:
        type 'ordered_pair', x, y
    """

    input_x = default.x
    input_y = default.y

    if default.type != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed for INTEGRATE"
        )

    if type(input_x) != np.ndarray:
        raise ValueError(f"Invalid type for x:{type(input_x)}")
    elif type(input_y) != np.ndarray:
        raise ValueError(f"Invalid type for y:{type(input_y)}")
    elif len(input_x) != len(input_y):
        raise ValueError(f"Invalid inputs, x:{input_x} y:{input_y}")

    integrate = trapz(input_x, input_y)

    return OrderedPair(x=input_x, y=integrate)
