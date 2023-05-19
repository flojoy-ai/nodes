import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def ABS(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Returns abolute value"""
    return DataContainer(x=dc_inputs[0].y, y=np.abs(dc_inputs[0].y))
