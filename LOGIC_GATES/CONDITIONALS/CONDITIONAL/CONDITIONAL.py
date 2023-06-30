from typing import Literal, Any
from flojoy import flojoy, DataContainer, JobResultBuilder, DefaultParams, OrderedPair  # type:ignore
from dataclasses import dataclass

@dataclass(frozen=True)  # Multiple outputs
class ConditionalOutput:
    true: DataContainer
    false: DataContainer

@flojoy
def CONDITIONAL(
    x: OrderedPair,
    y: OrderedPair,
    default_parmas: DefaultParams,
    operator_type: Literal["<=", ">", "<", ">=", "!=", "=="] = ">=",
) -> ConditionalOutput:
    """The CONDITIONAL node is a specialized node that compares two given DataContainer inputs
    and enqueues nodes connected with `true` or `false` output based on the comparison result.

    Parameters:
    -----------
    operator_type: str, optional
        Specifies the type of comparison to be performed between the two inputs. The default value is `>=`.
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
    # return (
    #     JobResultBuilder().from_data(data).flow_to_directions([next_direction]).build()
    # )
    return ConditionalOutput(true=data, false=data)


def compare_values(first_value: Any, second_value: Any, operator: str):
    bool_:bool = False
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
