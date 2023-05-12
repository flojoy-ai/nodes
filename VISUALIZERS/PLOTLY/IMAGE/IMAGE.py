from flojoy import flojoy, DataContainer
import plotly.express as px
import numpy as np


@flojoy
def IMAGE(dc_inputs, params):
    dc_input = dc_inputs[0]
    if dc_input.type == "image":
        r = dc_input.r
        g = dc_input.g
        b = dc_input.b
        a = dc_input.a
    else:
        raise ValueError("unsupported input type for IMAGE node")
    if a is None:
        img_combined = np.stack((r, g, b), axis=2)
    else:
        img_combined = np.stack((r, g, b, a), axis=2)
    fig = px.imshow(img=img_combined)

    return DataContainer(type="plotly", fig=fig, r=r, g=g, b=b, a=a)
