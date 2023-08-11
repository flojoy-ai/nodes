from flojoy import flojoy, Image, Plotly
import plotly.express as px
import numpy as np
from flojoy_nodes.VISUALIZERS.template import plot_layout


@flojoy
def IMAGE(default: Image) -> Plotly:
    """
    The IMAGE node creates a Plotly Image visualization for a given input data container type of image.

    Inputs
    ------
    default : Image
        the DataContainer to be visualized

    Outputs
    -------
    Plotly
        the DataContainer containing Plotly Image visualization of the input image
    """

    r = default.r
    g = default.g
    b = default.b
    a = default.a

    if a is None:
        img_combined = np.stack((r, g, b), axis=2)
    else:
        img_combined = np.stack((r, g, b, a), axis=2)
    layout = plot_layout(title="IMAGE")
    fig = px.imshow(img=img_combined)
    fig.layout = layout

    return Plotly(fig=fig)
