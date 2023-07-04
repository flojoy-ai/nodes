import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def CONSTANT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The CONSTANT node generates a single x-y vector of numeric
    (floating point) constants or a single scalar.

    Parameters
    ----------
    constant : float
        the constant value returned

    Returns:
    -------
    DataContainer:
        type 'ordered pair'
    """

    if dc_inputs.__len__() > 0:
        x = dc_inputs[0].y
        y = np.full(len(x), params["constant"])
        return DataContainer(x=x, y=y)

    else:
        return DataContainer(type="scalar", c=params["constant"])
