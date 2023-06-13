# from sympy import symbols, diff, parse_expr
from flojoy import flojoy, DataContainer
import numpy as np


@flojoy
def DIFFERENTIATE(dc_inputs : list[DataContainer], params: dict) -> DataContainer:
    dc_input = dc_inputs[0]

    if dc_input == "ordered_triple":
        input_x = dc_input.x
        input_y = dc_input.y
        if type(input) == "list":
            differentiate = np.diff(input_y) / np.diff(input_x)
        else:
            differentiate = np.diff(input_y) / input_x

        return DataContainer(type="ordered_pair", x=input_x, y=input_y, z=differentiate)

    else:
        raise ValueError(
           f"unsupported DataContainer type passed for DIFFERENTIATE : {dc_input.type}"
       )









    # if params["derivative"] != len(params["respective"]):
    #     raise ValueError(
    #         "Number of derivative that has to be performed does not match the respective variables"
    #     )
    
    # equation_str = params["equation"]

    # try:
    #     equation = parse_expr(equation_str)

    #     for resp in params["respective"]:
    #         derivative = diff(equation, symbols(resp))
    #         equation = derivative

    #     return DataContainer(type="ordered_pair", x=equation_str, y=derivative)

    # except Exception as e:
    #     print("Error:", e)