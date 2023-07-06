from flojoy import flojoy, OrderedPair
import numpy as np


@flojoy
def SELECT_ARRAY(default: OrderedPair, column: int = 0) -> OrderedPair:
    """
    Node to convert an input array with multiple columns
    to the selected ordered pair.

    For example, the SERIAL node can output x=time,
    y1=temperature, y2=pressure.
    This node will select one of temperature and pressure columns to output.

    The x axis will be return unchanged.
    """
    print("parameters passed to SELECT_ARRAY: ", column)
    # Index of the selected column.
    COL: int = column

    # Check for numpy type. Return unchanged data if not.
    if isinstance(default.y, np.ndarray):
        x: np.ndarray = default.x
        y: np.ndarray = default.y[:, int(COL)]

        return OrderedPair(x=x, y=y)

    else:
        return default
