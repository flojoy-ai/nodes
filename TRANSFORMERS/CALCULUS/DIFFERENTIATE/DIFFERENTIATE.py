from flojoy import flojoy, DataContainer
import numpy as np


@flojoy
def DIFFERENTIATE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    dc_input = dc_inputs[0]

    if dc_input.typee != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed for DIFFERENTIATE : {dc_input.type}"
        )

    input_x = dc_input.x
    input_y = dc_input.y

    differentiate = np.diff(input_y) / np.diff(input_x)

    return DataContainer(type="ordered_pair", x=input_x, y=differentiate)
