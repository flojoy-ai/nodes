from flojoy import flojoy, DataContainer
import numpy as np


@flojoy
def INTEGRATE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    dc_input = dc_inputs[0]

    if dc_input.type != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed for INTEGRATE : {dc_input.type}"
        )

    x = dc_input.x
    y = dc_input.y
    integrate = np.trapz(x, y)

    return DataContainer(type="ordered_pair", x=x, y=integrate)
