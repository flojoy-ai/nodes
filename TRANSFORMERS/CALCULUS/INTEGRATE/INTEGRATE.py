from flojoy import flojoy, DataContainer
import numpy as np


def trapz(x, y, n, m):
    if m[n] is not None:
        return m[n]
    if n == 0 or n == 1:
        trapezium = (1 / 2) * (x[0] + x[1]) * (y[1] - y[0])
    else:
        trapz(x, y, n - 1, m)
        trapezium = (1 / 2) * (x[n - 1] + x[n]) * (y[n] - y[n - 1])

    m[n] = trapezium

    return m[1:]


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
    numpy array / float
        integrated value in sequence of y array.
    """
    dc_input = dc_inputs[0]

    if dc_input.type != "ordered_pair" or dc_input.type != "ordered_triple":
        raise ValueError(
            f"unsupported DataContainer type passed for INTEGRATE : {dc_input.type}"
        )

    input_x = dc_input.x
    input_y = dc_input.y

    if type(input_x) != np.ndarray:
        raise ValueError(f"Invalid type for x:{type(input_x)}")
    elif type(input_y) != np.ndarray:
        raise ValueError(f"Invalid type for y:{type(input_y)}")
    elif len(input_x) != len(input_y):
        raise ValueError(f"Invalid inputs, x:{input_x} y:{input_y}")

    if dc_input.type == "ordered_pair":
        integrate = trapz(input_x, input_y, len(input_x) - 1, [None] * len(input_x))
        return DataContainer(type="ordered_pair", x=input_x, y=integrate)
    else:
        input_z = dc_input.z
        if type(input_z) != np.ndarray:
            raise ValueError(f"Invalid type for z:{type(input_z)}")
        elif len(input_x) != len(input_y) != len(input_z):
            raise ValueError(f"Invalid inputs, x:{input_x} y:{input_y} z:{input_z}")
        integrate = np.trapz(np.trapz(input_z, input_x), input_y)

        return DataContainer(type="ordered_triple", x=input_x, y=input_y, z=integrate)
