import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def SUBTRACT(
    x: DataContainer,
    y: DataContainer,
) -> DataContainer:
    """Subtract 2 input vectors and return the result"""
    if len(dc_inputs) < 2:
        raise ValueError(
            f"To substract the values, SUBSTRACT node requires two inputs, {len(dc_inputs)} was given!"
        )
    a = dc_inputs[0].y
    b = dc_inputs[1].y
    return DataContainer(x=x, y=y)
