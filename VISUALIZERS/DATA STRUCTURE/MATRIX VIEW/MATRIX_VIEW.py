from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
from plotly.graph_objects import Data
import numpy as np


def display_numpy_array_as_table(arr, max_cols, max_rows, placeholder):
    if arr.shape[0] > max_rows and arr.shape[1] > max_cols:
        new_arr = np.full((max_rows, max_cols), placeholder, dtype=object)
        new_arr[:-2, :-2] = arr[: max_rows - 2, : max_cols - 2]
        last_row = arr[arr.shape[0] - 1, :]
        first_cols = last_row[: max_rows - 2]
        new_arr[max_rows - 1, : max_cols - 2] = first_cols
        last_col = arr[:, arr.shape[1] - 1]
        first_rows = last_col[: max_cols - 2]
        new_arr[: max_rows - 2, max_cols - 1] = first_rows
        new_arr[max_rows - 1, max_cols - 1 :] = arr[
            arr.shape[0] - 1, arr.shape[1] - 1 :
        ]

    column_names = [f"Column {i+1}" for i in range(max_cols)]

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(line={"width":0}, values=[]),
                cells=dict(
                    values=new_arr.T, line={"width": 2}, height=80, align="center", format=[".4"]
                ),
            )
        ]
    )
    return fig


@flojoy
def MATRIX_VIEW(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly table visualization for a given input data container.

    Args:
    dc_inputs (list): A list of DataContainer object(s) containing the input data.
    params (dict): A dictionary containing the parameters needed for the visualization.

    Returns:
    DataContainer: A DataContainer object containing the generated visualization and the processed data.

    Raises:
    ValueError: If the input data container is not supported.
    """
    dc_input: DataContainer = DataContainer(type="ordered_pair", x=[0], y=[0])
    if dc_input.type:
        # Generate random matrix data
        matrix_data = np.array(
            [
                [4546556, 333521, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11],
                [1233333, 133333, 14, 15, 16, 17],
                [18, 19, 20, 21, 22, 23],
                [24, 25, 26, 27, 28, 29],
                [30, 31, 32, 33, 34, 35],
            ]
        )
        fig = display_numpy_array_as_table(matrix_data, 4, 4, r"$$$$\\ddots$$$$")

        print(
            " shape: ",
            matrix_data.shape,
            " size: ",
            matrix_data.size,
            " ndim: ",
            matrix_data.ndim,
            " dtype: ",
            matrix_data.dtype,
        )
        # data = Data([trace1])
        # table = go.Table(
        #     columnorder=[0, 1, 2, 3],
        #     columnwidth=[1] * 6,
        #     cells=dict(
        #         values=matrix_data, fill=dict(color="lavender"), align="center", height=80,

        #     ),
        # )
        width = 4 * 80 + 160
        height = width + 80
        fig.layout = go.Layout(
            autosize=False,
            width=width,
            height=height,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            hovermode="closest",
        )

        return DataContainer(type="plotly", fig=fig)
    else:
        raise ValueError(
            f"unsupported DataContainer type passed for MATRIX_VIEW: {dc_input.type}"
        )
