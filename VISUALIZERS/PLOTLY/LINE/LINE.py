from flojoy import flojoy, DataContainer
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def LINE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly Line visualization for a given input data container."""
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)
    match dc_input.type:
        case "ordered_pair":
            x = dc_input.x
            if isinstance(dc_input.x, dict):
                dict_keys = list(dc_input.x.keys())
                x = dc_input.x[dict_keys[0]]
            y = dc_input.y
            fig.add_trace(go.Line(x=x, y=y, mode="lines"))
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            for col in df.columns:
                fig.add_trace(go.Scatter(x=df.index, y=df[col], mode="lines", name=col))
                fig.update_layout(xaxis_title="X Axis", yaxis_title="Y Axis")
        case "matrix":
            fig.add_trace(go.Line(x=np.arange(len(dc_input.m)), y=dc_input.m))
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )
    return DataContainer(type="plotly", fig=fig)
