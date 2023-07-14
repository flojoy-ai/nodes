import plotly.graph_objects as go  # type:ignore
from flojoy import Plotly, OrderedTriple, DataFrame, flojoy, Surface, Matrix
from nodes.VISUALIZERS.template import plot_layout
import numpy as np


@flojoy
def SURFACE3D(default: OrderedTriple | DataFrame | Surface | Matrix) -> Plotly:
    """The SURFACE3D node creates a Plotly 3D Surface visualization for a given input data container.

    Parameters:
    -----------
    None

    Supported DC types:
    -------------------
    `ordered_triple`, `dataframe`, `surface`, `matrix`
    """
    layout = plot_layout(title="SURFACE3D")

    if isinstance(default, OrderedTriple):
        x = default.x
        y = default.y
        z = default.z
        if z.ndim < 2:
            num_columns = len(z) // 2
            z = np.reshape(z, (2, num_columns))
        fig = go.Figure(
            data=[go.Surface(x=x, y=y, z=z)],
            layout=layout,
        )
    elif isinstance(default, Surface):
        x = default.x
        y = default.y
        z = default.z
        fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)], layout=layout)
    elif isinstance(default, Matrix):
        m = default.m
        if m.ndim < 2:
            num_columns = len(m) // 2
            m = np.reshape(m, (2, num_columns))
        fig = go.Figure(data=[go.Surface(z=m)], layout=layout)
    else:
        df = default.m
        fig = go.Figure(data=[go.Surface(z=df.values)], layout=layout)

    return Plotly(fig=fig)
