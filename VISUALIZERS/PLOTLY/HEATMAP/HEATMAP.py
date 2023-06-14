from flojoy import flojoy, DataContainer
from nodes.VISUALIZERS.template import plot_layout
import numpy as np
import plotly.express as px


@flojoy
def HEATMAP(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly Heatmap visualization for a given input data container."""
    dc_inputs: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    match dc_inputs.type:
        case "grayscale":
           fig = px.imshow(dc_inputs.m)
        case "image":
            r = dc_inputs.r
            g = dc_inputs.g
            b = dc_inputs.b
            a = dc_inputs.a
            if a is None:
                img_combined = np.stack((r, g, b), axis=2)
            else:
                img_combined = np.stack((r, g, b, a), axis=2)
            fig = px.imshow(img_combined)
            fig.layout = layout
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_inputs.type}"
            )
    return DataContainer(type="plotly", fig=fig)