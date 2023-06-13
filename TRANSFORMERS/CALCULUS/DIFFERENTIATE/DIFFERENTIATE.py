from flojoy import flojoy, DataContainer
import numpy as np


@flojoy
def DIFFERENTIATE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
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
    dc_input = dc_inputs[0]

    if dc_input.type != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed for DIFFERENTIATE : {dc_input.type}"
        )

    input_x = dc_input.x
    input_y = dc_input.y

    if (
        type(input_x) != np.ndarray
        or type(input_y) != np.ndarray
        or len(input_x) != len(input_y)
    ):
        raise ValueError(f"Invalid inputs x:{input_x} y:{input_y}")

    differentiate = np.diff(input_y) / np.diff(input_x)

    return DataContainer(type="ordered_pair", x=input_x, y=differentiate)
