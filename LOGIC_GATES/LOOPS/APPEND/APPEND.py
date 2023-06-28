import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def APPEND(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The APPEND node appends a single data point to an array.
    The large array must be passed to the bottom "array" connection.
    For ordered pair: the single point must have a shape of 1 (or (1,)).

    Parameters
    ----------
    None

    Returns
    -------
    Ordered pair, dataframe or matrix.
    """

    if len(dc_inputs) < 2:
        raise ValueError(
            f"APPEND node requires two inputs, {len(dc_inputs)} was given!"
        )

    dc_input = dc_inputs[0]

    match dc_input.type:
        case "ordered_pair":
            y0 = dc_inputs[0].y
            y1 = dc_inputs[1].y

            x0 = dc_inputs[0].x
            x1 = dc_inputs[1].x

            if y1.shape[0] != 1:
                raise ValueError(
                    (
                        "To append, APPEND node the requires the non-array "
                        "input to have a single point. "
                        f"The data passed has a shape of: {y1.shape}"
                    )
                )

            y = np.append(y0, y1)
            x = np.append(x0, x1)

            return DataContainer(x=x, y=y)

        case "matrix":
            m0 = dc_inputs[0].m
            m1 = dc_inputs[1].m

            m = np.append(m0, m1)

            return DataContainer(type="matrix", m=m)

        case "dataframe":
            m0 = dc_inputs[0].m
            m1 = dc_inputs[1].m

            df = np.append(m0, m1)

            return DataContainer(type="dataframe", m=df)
