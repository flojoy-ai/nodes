from flojoy import flojoy, OrderedPair, OrderedTriple, DataFrame, Vector, Plotly
import plotly.graph_objects as go
import pandas as pd
from flojoy_nodes.VISUALIZERS.template import plot_layout


@flojoy
def TABLE(default: OrderedTriple | OrderedPair | DataFrame | Vector) -> Plotly:
    """The TABLE node creates a Plotly Table visualization for a given input data container.

    Inputs
    ------
    default : OrderedTriple|OrderedPair|DataFrame|Vector
        the DataContainer to be visualized

    Returns
    -------
    Plotly
        the DataContainer containing Plotly Table visualization

    """

    layout = plot_layout(title="TABLE")
    fig = go.Figure(layout=layout)

    match default:
        case OrderedPair():
            x = default.x
            y = default.y
            fig.add_trace(
                go.Table(
                    header=dict(values=["x", "y"], align="center"),
                    cells=dict(values=[x, y], align="center"),
                )
            )
        case OrderedTriple():
            x = default.x
            y = default.y
            z = default.z
            fig.add_trace(
                go.Table(
                    header=dict(values=["x", "y", "z"], align="center"),
                    cells=dict(values=[x, y, z], align="center"),
                )
            )
        case Vector():
            v = default.v
            fig.add_trace(
                go.Table(
                    header=dict(values=["v"], align="center"),
                    cells=dict(values=[v], align="center"),
                )
            )
        case DataFrame():
            df = pd.DataFrame(default.m)
            fig.add_trace(
                go.Table(
                    header=dict(values=list(df.columns), align="center"),
                    cells=dict(values=[df[col] for col in df.columns], align="center"),
                )
            )
    return Plotly(fig=fig)
