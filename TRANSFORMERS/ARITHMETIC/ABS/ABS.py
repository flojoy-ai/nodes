import numpy as np
from flojoy import flojoy, DataContainer, DefaultParams


@flojoy
def ABS(default: DataContainer, default_params: DefaultParams) -> DataContainer:
    """Returns abolute value"""
    return DataContainer(x=dc_inputs[0].y, y=np.abs(dc_inputs[0].y))
