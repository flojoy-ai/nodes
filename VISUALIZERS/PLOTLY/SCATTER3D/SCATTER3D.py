import plotly.graph_objects as go
import plotly.express as px
from flojoy import OrderedTriple, DataFrame, Plotly, flojoy
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def SCATTER3D(default: OrderedTriple | DataFrame) -> Plotly:
    """The SCATTER3D node creates a Plotly 3D Scatter visualization for a given input DataContainer.

    Inputs
    ------
    default : OrderedTriple|DataFrame
        the DataContainer to be visualized

    Returns
    -------
    Plotly
        the DataContainer containing the Plotly 3D Scatter visualization
    """

    layout = plot_layout(title="SCATTER3D")
    fig = go.Figure(layout=layout)
    match default:
        case OrderedTriple():
            x = default.x
            if isinstance(default.x, dict):
                dict_keys = list(default.x.keys())
                x = default.x[dict_keys[0]]
            y = default.y
            z = default.z
            fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode="markers"))
        case DataFrame():
            df = default.m
            if len(df.columns) < 3:
                raise ValueError(
                    "DataFrame must have at least 3 columns for x, y, and z coordinates."
                )

            x_column = df.columns[0]
            y_column = df.columns[1]
            z_column = df.columns[2]

            fig = px.scatter_3d(df, x=x_column, y=y_column, z=z_column, color=z_column)

    return Plotly(fig=fig)
