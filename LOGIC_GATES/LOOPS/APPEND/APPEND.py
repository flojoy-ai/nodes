import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def APPEND(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The APPEND node appends a single data point to an array.
    Ordered pair type must be used for both the data point
    and the array.

    Parameters
    ----------
    None

    Returns
    -------
    Ordered pair.
    """

    if len(dc_inputs) < 2:
        raise ValueError(
            f"To append, APPEND node requires two inputs, {len(dc_inputs)} was given!"
        )
    y0 = dc_inputs[0].y
    y1 = dc_inputs[1].y

    x0 = dc_inputs[0].x
    x1 = dc_inputs[1].x

    y = np.append(y0, y1)
    x = np.append(x0, x1)

    return DataContainer(x=x, y=y)
