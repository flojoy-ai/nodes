import plotly.graph_objects as go
from flojoy import DataContainer, flojoy


@flojoy
def SCATTER3D(dc_inputs, params):
    dc_input = dc_inputs[0]
    if dc_input.type == "ordered_triple":
        x = dc_input.x
        if isinstance(dc_input.x, dict):
            dict_keys = list(dc_input.x.keys())
            x = dc_input.x[dict_keys[0]]
        y = dc_input.y
        z = dc_input.z
    else:
        raise ValueError("unsupported input type for SCATTER3D node")
    fig = go.Figure(data=go.Scatter3d(x=x, y=y, z=z, mode="markers"))
    return DataContainer(type="plotly", fig=fig, x=x, y=y, z=z)
