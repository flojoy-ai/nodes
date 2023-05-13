import plotly.graph_objects as go
from flojoy import flojoy, DataContainer
import pandas as pd


@flojoy
def SCATTER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly Scatter visualization for a given input data container."""
    dc_input = dc_inputs[0]
    fig = go.Figure()
    match dc_input.type:
        case "ordered_pair":
            x = dc_input.x
            if isinstance(dc_input.x, dict):
                dict_keys = list(dc_input.x.keys())
                x = dc_input.x[dict_keys[0]]
            y = dc_input.y
            fig.add_trace(go.Scatter(x=x, y=y, mode="markers"))
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            for col in df.columns:
                fig.add_trace(
                    go.Scatter(x=df[col], y=df.index, mode="markers", name=col)
                )
            fig.update_layout(
                title="Scatter Plot", xaxis_title="X Axis", yaxis_title="Y Axis"
            )
        case _:
            raise ValueError("unsupported DataContainer type for SCATTER node")
    return DataContainer(type="plotly", fig=fig)
