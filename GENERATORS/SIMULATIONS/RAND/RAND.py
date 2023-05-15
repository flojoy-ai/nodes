import numpy as np
from flojoy import flojoy, DataContainer
import traceback


@flojoy
def RAND(dc_inputs, params):
    x = None
    if len(dc_inputs) > 0:
        x = dc_inputs[0].y
        y = np.random.normal(size=len(x))
    else:
        y = np.random.normal(size=1000)

    return DataContainer(x=x, y=y)


@flojoy
def RAND_MOCK(dc_inputs, params):
    print("running mock version of rand")
    x = None
    if len(dc_inputs) > 0:
        x = dc_inputs[0].y
        y = x
    else:
        y = np.full(
            1000, 1000
        )  # for reproducibility returning an array with constant values
    return DataContainer(x=x, y=y)
