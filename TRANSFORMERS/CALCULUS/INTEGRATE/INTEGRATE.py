from flojoy import flojoy, DataContainer
import numpy as np


def trapz(x, y):
    m = [0] * len(x)
    trapezium = (1 / 2) * (x[0] + x[1]) * (y[1] - y[0])
    m[1] = trapezium

    for i in range(2, len(x)):
        trapezium = (1 / 2) * (x[i - 1] + x[i]) * (y[i] - y[i - 1])
        m[i] = trapezium

    return m


@flojoy
def INTEGRATE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
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
    dc_input = dc_inputs[0]

    input_x = dc_input.x
    input_y = dc_input.y

    if dc_input.type != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed for INTEGRATE : {dc_input.type}"
        )

    if type(input_x) != np.ndarray:
        raise ValueError(f"Invalid type for x:{type(input_x)}")
    elif type(input_y) != np.ndarray:
        raise ValueError(f"Invalid type for y:{type(input_y)}")
    elif len(input_x) != len(input_y):
        raise ValueError(f"Invalid inputs, x:{input_x} y:{input_y}")

    integrate = trapz(input_x, input_y)

    return DataContainer(type="ordered_pair", x=input_x, y=integrate)
