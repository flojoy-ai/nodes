from typing import Any, TypedDict, Literal
from flojoy import flojoy, JobResultBuilder, OrderedPair


class ConditionalOutput(TypedDict):
    true: Any
    false: Any


@flojoy
def CONDITIONAL(
    x: OrderedPair,
    y: OrderedPair,
    operator_type: Literal["<=", ">", "<", ">=", "!=", "=="] = ">=",
) -> ConditionalOutput:
    """
    The CONDITIONAL node is a specialized node that compares two given DataContainer inputs. 
    
    It then enqueues nodes connected with a "true" or "false" output based on the comparison result.

    Parameters
    ----------
    operator_type : str, optional
        Specifies the type of comparison to be performed between the two inputs. The default value is ">=".
    """

    y_of_x = x.y
    y_of_y = y.y
    bool_ = compare_values(y_of_x[0], y_of_y[0], operator_type)
    data = None
    if operator_type in ["<=", "<"]:
        if not bool_:
            data = OrderedPair(x=x.x, y=y.y)
        else:
            data = OrderedPair(x=y.x, y=x.y)
    elif bool_:
        data = OrderedPair(x=x.x, y=y.y)
    else:
        data = OrderedPair(x=y.x, y=x.y)
    next_direction = str(bool_).lower()
    return ConditionalOutput(
        true=JobResultBuilder()
        .from_data(data)
        .flow_to_directions([next_direction])
        .build(),
        false=JobResultBuilder()
        .from_data(data)
        .flow_to_directions([next_direction])
        .build(),
    )


def compare_values(first_value: Any, second_value: Any, operator: str):
    bool_: bool = False
    if operator == "<=":
        bool_ = first_value <= second_value
    elif operator == ">":
        bool_ = first_value > second_value
    elif operator == "<":
        bool_ = first_value < second_value
    elif operator == ">=":
        bool_ = first_value >= second_value
    elif operator == "!=":
        bool_ = first_value != second_value
    else:
        bool_ = first_value == second_value
    return bool_
