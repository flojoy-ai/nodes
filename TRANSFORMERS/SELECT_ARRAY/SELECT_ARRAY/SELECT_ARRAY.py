from flojoy import flojoy, DataContainer
import numpy as np


@flojoy
def SELECT_ARRAY(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Node to convert an input array with multiple columns
    to the selected ordered pair.

    For example, the SERIAL node can output x=time,
    y1=temperature, y2=pressure.
    This node will select one of temperature and pressure columns to output.

    The x axis will be return unchanged.
    """
    print("parameters passed to SELECT_ARRAY: ", params)
    # Index of the selected column.
    COL = int(params.get("column", 0))

    # Check for numpy type. Return unchanged data if not.
    if isinstance(dc_inputs[0].y, np.ndarray):
        x = dc_inputs[0].x
        y = dc_inputs[0].y[:, int(COL)]

        return DataContainer(x=x, y=y)

    else:
        return dc_inputs[0]
