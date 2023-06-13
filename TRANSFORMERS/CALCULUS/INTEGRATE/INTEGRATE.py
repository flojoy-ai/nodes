from flojoy import flojoy, DataContainer
import numpy as np


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

    if dc_input.type != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed for INTEGRATE : {dc_input.type}"
        )

    x = dc_input.x
    y = dc_input.y

    if type(x) != np.ndarray or type(y) != np.ndarray or len(x) != len(y):
        raise ValueError(f"Invalid inputs x:{x} y:{y}")

    integrate = np.trapz(x, y)

    return DataContainer(type="ordered_pair", x=x, y=integrate)
