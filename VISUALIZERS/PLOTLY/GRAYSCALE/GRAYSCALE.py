from flojoy import flojoy, DataContainer
from nodes.VISUALIZERS.template import plot_layout
from PIL import Image
import numpy as np
import plotly.express as px



@flojoy
def GRAYSCALE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly Heatmap visualization for a given input data container."""
    dc_inputs: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    match dc_inputs.type:
        case "grayscale":
            grayscale = dc_inputs.m
            print(grayscale)
            return DataContainer(type="image", r=grayscale, g=grayscale, b=grayscale, a=None)
        case "image":
            r = dc_inputs.r
            g = dc_inputs.g
            b = dc_inputs.b
            a = dc_inputs.a
            if a is None:
                rgba_image = np.stack((r, g, b), axis=2)
            else:
                rgba_image = np.stack((r, g, b, a), axis=2)
            #convert into grayscale for heatmap
            image = Image.fromarray(rgba_image)
            image = image.convert("L")
            grayscale = np.array(image)
        case _:
                raise ValueError(
                    f"unsupported DataContainer type passed for {node_name}: {dc_inputs.type}"
                )
    return DataContainer(type="image", r=grayscale, g=grayscale, b=grayscale, a=None)