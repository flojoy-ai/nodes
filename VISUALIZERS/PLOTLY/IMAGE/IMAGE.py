from flojoy import flojoy, DataContainer, DefaultParams
import plotly.express as px
import numpy as np
from nodes.VISUALIZERS.template import plot_layout

@flojoy
def IMAGE(default: DataContainer, default_parmas: DefaultParams) -> DataContainer:
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split('.')[-1]
    if dc_input.type == 'image':
        r = dc_input.r
        g = dc_input.g
        b = dc_input.b
        a = dc_input.a
    else:
        raise ValueError(f'unsupported DataContainer type passed for {node_name}: {dc_input.type}')
    if a is None:
        img_combined = np.stack((r, g, b), axis=2)
    else:
        img_combined = np.stack((r, g, b, a), axis=2)
    layout = plot_layout(title='IMAGE')
    fig = px.imshow(img=img_combined)
    fig.layout = layout
    return DataContainer(type='plotly', fig=fig, r=r, g=g, b=b, a=a)