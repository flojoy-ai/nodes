import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def ABS(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The ABS node returns the absolute value for the input.
    The node can handle scalar and ordered pair inputs currently

    TODO - reconcile.py so matrix and dataframe types can be handled.

    Parameters
    ----------
    None

    Returns:
    --------
    DataContainer:
        type 'ordered pair' if 'ordered pair' is input.

        type 'scalar' if 'scalar' is input.
    """

    match dc_inputs[0].type:
        case "scalar":
            return DataContainer(type='scalar', c=np.abs(dc_inputs[0].c))

        case "ordered_pair":
            return DataContainer(x=dc_inputs[0].x, y=np.abs(dc_inputs[0].y))
