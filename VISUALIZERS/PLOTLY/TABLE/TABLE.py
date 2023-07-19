from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout
import numpy as np


@flojoy
def TABLE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The TABLE node creates a Plotly table visualization for a given input data container.

    Parameters:
    -----------
    None

    Supported DC types:
    -------------------
    `ordered_pair`, `dataframe`, `ordered_triple`
    """
    dc_input = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)
    match dc_input.type:
        case "ordered_pair":
            x = dc_input.x
            y = dc_input.y
            fig.add_trace(
                go.Table(
                    header=dict(values=["x", "y"], align="center"),
                    cells=dict(values=[x, y], align="center"),
                )
            )
        case "ordered_triple":
            x = dc_input.x
            y = dc_input.y
            z = dc_input.z
            fig.add_trace(
                go.Table(
                    header=dict(values=["x", "y", "z"], align="center"),
                    cells=dict(values=[x, y, z], align="center"),
                )
            )
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            fig.add_trace(
                go.Table(
                    header=dict(values=list(df.columns), align="center"),
                    cells=dict(values=[df[col] for col in df.columns], align="center"),
                )
            )

        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )
    return DataContainer(type="plotly", fig=fig)
