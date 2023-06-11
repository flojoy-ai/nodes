from flojoy import flojoy, DataContainer, JobResultBuilder
from typing import Union
from utils.utils import compare_values


@flojoy
def CONDITIONAL(
    dc_inputs: list[DataContainer], params: dict
) -> Union[DataContainer, dict]:
    """The CONDITIONAL node is a specialized node that compares two given DataContainer inputs
    and enqueues nodes connected with `true` or `false` output based on the comparison result.

    Parameters:
    -----------
    operator_type: str, optional
        Specifies the type of comparison to be performed between the two inputs. The default value is `>=`.
    """
    operator = params["operator_type"]

    dc_input_x = dc_inputs[0]
    dc_input_y = dc_inputs[1]
    x = dc_input_x.y
    y = dc_input_y.y
    bool_ = compare_values(x[0], y[0], operator)

    data = None
    if operator in ["<=", "<"]:
        if not bool_:
            data = DataContainer(x=dc_inputs[0].x, y=y)
        else:
            data = DataContainer(x=dc_inputs[1].x, y=x)
    else:
        if bool_:
            data = DataContainer(x=dc_inputs[0].x, y=y)
        else:
            data = DataContainer(x=dc_inputs[1].x, y=x)

    next_direction = str(bool_).lower()

    return (
        JobResultBuilder().from_data(data).flow_to_directions([next_direction]).build()
    )
