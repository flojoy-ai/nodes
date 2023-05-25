from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import numpy as np


CELL_SIZE = 50
FONT_SIZE = 10
MAX_ALLOWED_SHAPE = 10
v_dot = "$\\vdots$"
d_dot = "$\\ddots$"
l_dot = "$\\ldots$"


def display_numpy_array_as_table(arr, shape_size, placeholder):
    new_arr = arr
    max_shape_size = shape_size
    if arr.shape[0] > max_shape_size:
        new_arr = np.full((max_shape_size, max_shape_size), placeholder, dtype=object)
        new_arr[:-2, :-2] = arr[: max_shape_size - 2, : max_shape_size - 2]
        last_row = arr[arr.shape[0] - 1, :]
        first_cols = last_row[: max_shape_size - 2]
        new_arr[max_shape_size - 1, : max_shape_size - 2] = first_cols
        last_col = arr[:, arr.shape[1] - 1]
        first_rows = last_col[: max_shape_size - 2]
        new_arr[: max_shape_size - 2, max_shape_size - 1] = first_rows
        new_arr[max_shape_size - 1, max_shape_size - 1 :] = arr[
            arr.shape[0] - 1, arr.shape[1] - 1 :
        ]
        new_arr[0, max_shape_size - 2] = l_dot
        new_arr[max_shape_size - 1, max_shape_size - 2] = l_dot

        new_arr[max_shape_size - 2, 0] = v_dot
        new_arr[max_shape_size - 2, max_shape_size - 1] = v_dot

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(line={"width": 0}, values=[]),
                cells=dict(
                    values=new_arr.T,
                    line={"width": 2},
                    font={"size": FONT_SIZE},
                    height=CELL_SIZE,
                    align="center",
                    format=[".3"],
                ),
            )
        ]
    )
    return fig


@flojoy
def MATRIX_VIEW(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    dc_input = dc_inputs[0]
    if dc_input.type == "matrix":
        matrix_data = dc_input.m
        ndim = matrix_data.ndim
        if ndim < 2 or ndim > 2:
            raise ValueError("MATRIX_VIEW can process only 2D arrays!")
        row_shape, col_shape = matrix_data.shape
        if row_shape != col_shape:
            raise ValueError("Rows and columns must be of same shape!")

        fig = display_numpy_array_as_table(matrix_data, MAX_ALLOWED_SHAPE, r"$\ddots$")
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
    else:
        raise ValueError(
            f"unsupported DataContainer type passed for MATRIX_VIEW: {dc_input.type}"
        )
