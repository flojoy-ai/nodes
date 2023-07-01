import plotly.graph_objects as go
from flojoy import DataContainer, flojoy, DefaultParams
from nodes.VISUALIZERS.template import plot_layout
import pandas as pd


@flojoy
def SURFACE3D(default: DataContainer, default_params: DefaultParams) -> DataContainer:
    """The SURFACE3D node creates a Plotly 3D Surface visualization for a given input data container.

    Parameters:
    -----------
    None

    Supported DC types:
    -------------------
    `ordered_triple`, `dataframe`
    """
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)
    match dc_input.type:
        case "ordered_triple":
            x = dc_input.x
            y = dc_input.y
            z = dc_input.z
            fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)], layout=layout)
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            fig = go.Figure(data=go.Surface(z=df.values), layout=layout)
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )
    return DataContainer(type="plotly", fig=fig)
