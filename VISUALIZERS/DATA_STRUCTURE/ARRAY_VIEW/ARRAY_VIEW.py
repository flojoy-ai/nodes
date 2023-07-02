from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import numpy as np
import pandas as pd

CELL_SIZE = 50
FONT_SIZE = 10
MAX_ALLOWED_SHAPE = 10
l_dot = "$\\ldots$"


def numpy_array_as_table(arr: np.ndarray, placeholder: str):
    if arr.size > MAX_ALLOWED_SHAPE:
        converted_type = arr.astype(object)
        new_arr = converted_type[:MAX_ALLOWED_SHAPE]
        new_arr[MAX_ALLOWED_SHAPE - 2] = l_dot
    else:
        new_arr = arr
    return new_arr.reshape(-1, 1)


@flojoy
def ARRAY_VIEW(
    default: DataContainer,
) -> DataContainer:
    """
    The ARRAY_VIEW node takes "ordered_pair", "dataframe", "matrix", and "image" as input type
    and displays its visualization in array format.

    Parameters
    ----------
    None

    Returns
    -------
    plotly
        Visualization of the input data in array format
    """
    dc_input = dc_inputs[0]
    match dc_input.type:
        case "ordered_pair":
            data = dc_input.y
            cell_values = numpy_array_as_table(data, l_dot)
        case "dataframe":
            data = pd.DataFrame(dc_input.m).to_numpy(dtype=object)
            data = data[:, :-1]
            cell_values = numpy_array_as_table(data, l_dot)
        case "matrix":
            data = dc_input.m
            cell_values = numpy_array_as_table(data, l_dot)
        case "image":
            red = dc_input.r
            green = dc_input.g
            blue = dc_input.b
            if dc_input.a == None:
                merge = np.stack((red, green, blue), axis=2)
            else:
                alpha = dc_inputs[0].a
                merge = np.stack((red, green, blue, alpha), axis=2)
            merge = merge.reshape(-1, merge.shape[-1])
            cell_values = numpy_array_as_table(merge, l_dot)
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for ARRAY_VIEW: {dc_input.type}"
            )
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(line={"width": 0}, values=[]),
                cells=dict(
                    values=cell_values,
                    line={"width": 3},
                    font={"size": FONT_SIZE},
                    height=CELL_SIZE,
                    align="center",
                    format=[".3"],
                ),
            )
        ]
    )
    if dc_input.type == "image" or dc_input.type == "dataframe":
        width = MAX_ALLOWED_SHAPE * CELL_SIZE + 800
    else:
        width = MAX_ALLOWED_SHAPE * CELL_SIZE + 80
    height = width + 80
    fig.layout = go.Layout(
        autosize=False,
        width=width,
        height=height,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        hovermode="closest",
        font=dict(size=FONT_SIZE),
    )
    return DataContainer(type="plotly", fig=fig)
