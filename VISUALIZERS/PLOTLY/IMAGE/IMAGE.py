from flojoy import flojoy, Image, Plotly
import plotly.express as px
import numpy as np
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def IMAGE(default: Image) -> Plotly:
    node_name = __name__.split(".")[-1]
    r = default.r
    g = default.g
    b = default.b
    a = default.a

    if a is None:
        img_combined = np.stack((r, g, b), axis=2)
    else:
        img_combined = np.stack((r, g, b, a), axis=2)
    layout = plot_layout(title=node_name)
    fig = px.imshow(img=img_combined)
    fig.layout = layout

    return Plotly(fig=fig)
