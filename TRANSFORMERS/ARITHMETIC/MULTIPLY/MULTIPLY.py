import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def MULTIPLY(dc_inputs, params):
    """Takes 2 input vectors, multiplies them, and returns the result"""
    a = dc_inputs[0].y
    b = dc_inputs[1].y

    x = dc_inputs[0].x
    y = np.multiply(a, b)

    return DataContainer(x=x, y=y)
