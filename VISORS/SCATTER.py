import plotly.graph_objects as go
from flojoy import flojoy, DataContainer


@flojoy
def SCATTER(v, params):
    dc_input = v[0]
    if dc_input.type == 'ordered_pair':
        x = dc_input.x
        if isinstance(dc_input.x, dict):
            dict_keys = list(dc_input.x.keys())
            x = dc_input.x[dict_keys[0]]
        y = dc_input.y
    else:
        raise ValueError('unsupported input type for SCATTER node')
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
    return DataContainer(type='plotly', fig=fig, x=x, y=y)