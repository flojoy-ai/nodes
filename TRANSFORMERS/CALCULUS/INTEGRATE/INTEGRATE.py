from sympy import symbols, parse_expr, integrate
from flojoy import flojoy, DataContainer

@flojoy
def INTEGRATE(dc_inputs : list[DataContainer], params : dict) -> DataContainer:
    equation_str = params["equation"]

    x = symbols('x')

    if params["integral"] == "DOUBLE":
        y = symbols('y')
    elif params["integral"] == "TRIPLE":
        y = symbols('y')
        z = symbols('z')

    try:
        equation = parse_expr(equation_str)
        if params["bounds"]:
            if params["integral"] == "SINGLE":
                integral = integrate(equation, (x, params["first_integral_upper_bound"], params["first_integral_lower_bound"]))
            elif params["integral"] == "DOUBLE":
                integral = integrate(equation, (x, params["first_integral_upper_bound"], params["first_integral_lower_bound"]),
                                      (y, params["second_integral_upper_bound"], params["second_integral_lower_bound"]))
            elif params["integral"] == "TRIPLE":
                integral = integrate(equation, (x, params["first_integral_upper_bound"], params["first_integral_lower_bound"]), 
                                     (y, params["second_integral_upper_bound"], params["second_integral_lower_bound"]),
                                     (z, params["third_integral_upper_bound"], params["thrid_integral_lower_bound"]))
        
        else:
            if params["integral"] == "SINGLE":
                integral = integrate(equation, x)
            elif params["integral"] == "DOUBLE":
                integral = integrate(equation, x, y)
            elif params["integral"] == "TRIPLE":
                integral = integrate(equation, x, y, z)

        return DataContainer(type="ordered_pair", x=equation_str, y=integral)

    except Exception as e:
        print("Error:", e)