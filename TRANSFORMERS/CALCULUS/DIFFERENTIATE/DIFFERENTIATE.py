from sympy import symbols, diff, parse_expr
from flojoy import flojoy, DataContainer


@flojoy
def DIFFERENTIATE(dc_inputs : list[DataContainer], params: dict) -> DataContainer:

    if params["derivative"] != len(params["respective"]):
        raise ValueError(
            "Number of derivative that has to be performed does not match the respective variables"
        )
    
    equation_str = params["equation"]

    try:
        equation = parse_expr(equation_str)

        for resp in params["respective"]:
            derivative = diff(equation, symbols(resp))
            equation = derivative

        return DataContainer(type="ordered_pair", x=equation_str, y=derivative)

    except Exception as e:
        print("Error:", e)