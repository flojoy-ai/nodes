from flojoy import (
    flojoy,
    OrderedPair,
    Scalar,
    Vector,
)


@flojoy(node_type="BIG_NUMBER", forward_result=True)
def BIG_NUMBER(
    default: OrderedPair | Scalar | Vector, scientific_notation: bool = False
) -> Scalar:
    """The BIG_NUMBER node generates a Plotly figure, displaying a big number with an optional prefix and suffix.

    Inputs
    ------
    default : OrderedPair|Scalar|Vector
        the DataContainer to be visualized

    Parameters
    ----------
    relative_delta : bool
        whether or not to show the relative delta from the last run along with big number
    suffix : str
        any suffix to show with big number
    prefix : str
        any prefix to show with big number
    title : str
        title of the plot, default = "BIG_NUMBER"

    Returns
    -------
    Plotly
        the DataContainer containing the Plotly big number visualization
    """

    match default:
        case OrderedPair():
            return Scalar(default.y[-1])
        case Scalar():
            return Scalar(default.c)
        case Vector():
            return Scalar(default.v[-1])
        case _:
            raise ValueError(f"Invalid input type {type(default)} for node {node_name}")
