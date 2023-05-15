import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def LINSPACE(dc_inputs, params):
    x = None
    if dc_inputs.__len__() > 0:
        x = dc_inputs[0].y
    y = np.linspace(float(params["start"]), float(params["end"]), int(params["step"]))
    result = DataContainer(x=x, y=y)
    return result
