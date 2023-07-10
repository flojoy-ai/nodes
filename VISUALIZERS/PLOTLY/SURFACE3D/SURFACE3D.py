import plotly.graph_objects as go
from flojoy import Plotly, OrderedTriple, DataFrame, flojoy
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def SURFACE3D(default: OrderedTriple | DataFrame) -> Plotly:
    """The SURFACE3D node creates a Plotly 3D Surface visualization for a given input data container.

    Parameters:
    -----------
    None

    Supported DC types:
    -------------------
    `ordered_triple`, `dataframe`
    """
    layout = plot_layout(title="SURFACE3D")

    if isinstance(default, OrderedTriple):
        x = default.x
        y = default.y
        z = default.z
        fig = go.Figure(
            data=[
                go.Surface(x=x, y=y, z=z),
            ],
            layout=layout,
        )
    else:
        df = default.m
        fig = go.Figure(data=go.Surface(z=df.values), layout=layout)

    return Plotly(fig=fig)
