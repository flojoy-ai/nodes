import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def MATMUL(dc_inputs, params):
    """Takes 2 input matrices, multiplies them, and returns the result"""
    a = np.eye(3)
    b = np.eye(3)
    if len(dc_inputs) == 2:
        a = dc_inputs[0].y
        b = dc_inputs[1]["y"]
    return DataContainer(type="matrix", m=np.matmul(a, b))
