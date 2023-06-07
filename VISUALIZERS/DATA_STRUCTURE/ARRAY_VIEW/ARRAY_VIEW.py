from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import numpy as np
import pandas as pd

CELL_SIZE = 50
FONT_SIZE = 10
v_dot = "$\\vdots$"
d_dot = "$\\ddots$"
l_dot = "$\\ldots$"


@flojoy
def MATRIX_VIEW(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    dc_input = dc_inputs[0]

    match dc_input.type:
        case "matrix":
            data = np.asarray(dc_input.m)
        case "dataframe":
            data = pd.DataFrame(dc_input).to_numpy()
    fig = go.Figure(
        go.Box
    )

    return DataContainer(type="plotly")