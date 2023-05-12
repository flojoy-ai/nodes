import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def ADD(dc_inputs, params):
    """Add 2 input vectors and return the result"""
    # print(' dc_inputs in add node: ', dc_inputs)
    a = [0]
    b = [0]

    if len(dc_inputs) == 2:
        a = dc_inputs[0].y
        b = dc_inputs[1]["y"]

    y = np.add(a, b)

    return DataContainer(x={"a": a, "b": b}, y=y)
