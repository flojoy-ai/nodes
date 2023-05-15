import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def ADD(dc_inputs: list[DataContainer], params: dicts):
    """Add 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is added to an array or matrix, each element in the array or
    matrix will be increased by the constant value. If 2 arrays or matrices of different
    sizes are added, the output will be the size of the larger array or matrix with
    only the overlapping elements changed.
    """

    a = [0]
    b = [0]

    if len(v) == 2:
        a = v[0].y
        b = v[1]["y"]

    y = np.add(a, b)

    return DataContainer(x={"a": a, "b": b}, y=y)
