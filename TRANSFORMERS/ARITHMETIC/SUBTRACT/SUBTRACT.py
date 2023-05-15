import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def SUBTRACT(dc_inputs, params):
    """Subtract 2 input vectors and return the result"""
    # print(' v in add node: ', v)
    a = [0]
    b = [0]

    if len(dc_inputs) == 2:
        a = dc_inputs[0].y
        b = dc_inputs[1]["y"]

    y = np.subtract(a, b)

    return DataContainer(x={"a": a, "b": b}, y=y)
