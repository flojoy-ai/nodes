import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def APPEND(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The APPEND node appends a single data point to an array.
    The large array must be passed to the bottom "array" connection.
    The single point must have a shape of 1 (or (1,)).

    Parameters
    ----------
    None

    Returns
    -------
    Ordered pair (numpy arrays).
    """

    if len(dc_inputs) < 2:
        raise ValueError(
            f"To append, APPEND node requires two inputs, {len(dc_inputs)} was given!"
        )
    y0 = dc_inputs[0].y
    y1 = dc_inputs[1].y

    x0 = dc_inputs[0].x
    x1 = dc_inputs[1].x

    if y1.shape[0] != 1:
        raise ValueError(
            (
                "To append, APPEND node the requires the non-array input to have "
                f"a single point. The data passed has a shape of: {y1.shape}"
            )
        )

    y = np.append(y0, y1)
    x = np.append(x0, x1)

    return DataContainer(x=x, y=y)
