import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def LINSPACE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    x = None
    if dc_inputs.__len__() > 0:
        x = dc_inputs[0].y
    y = np.linspace(params["start"], params["end"], params["step"])
    result = DataContainer(x=x, y=y)
    return result
