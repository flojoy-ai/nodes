from flojoy import flojoy, OrderedPair, OrderedTriple, DataFrame, Plotly
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def TABLE(default: OrderedTriple | OrderedPair | DataFrame) -> Plotly:
    """The TABLE node creates a Plotly table visualization for a given input data container.

    Parameters:
    -----------
    None

    Supported DC types:
    -------------------
    `ordered_pair`, `dataframe`, `ordered_triple`
    """
    layout = plot_layout(title="TABLE")
    fig = go.Figure(layout=layout)

    if isinstance(default, OrderedPair):
        x = default.x
        y = default.y
        fig.add_trace(
            go.Table(
                header=dict(values=["x", "y"], align="center"),
                cells=dict(values=[x, y], align="center"),
            )
        )
    elif isinstance(default, OrderedTriple):
        x = default.x
        y = default.y
        z = default.z
        fig.add_trace(
            go.Table(
                header=dict(values=["x", "y", "z"], align="center"),
                cells=dict(values=[x, y, z], align="center"),
            )
        )
    else:
        df = pd.DataFrame(default.m)
        fig.add_trace(
            go.Table(
                header=dict(values=list(df.columns), align="center"),
                cells=dict(values=[df[col] for col in df.columns], align="center"),
            )
        )
    return Plotly(fig=fig)
