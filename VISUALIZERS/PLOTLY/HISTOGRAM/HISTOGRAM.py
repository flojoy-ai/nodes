from flojoy import flojoy, DataContainer
import plotly.express as px


@flojoy
def HISTOGRAM(v, params):
    dc_input = v[0]
    if dc_input.type == "ordered_pair":
        x = dc_input.x
        if isinstance(dc_input.x, dict):
            dict_keys = list(dc_input.x.keys())
            x = dc_input.x[dict_keys[0]]
        y = dc_input.y
    else:
        raise ValueError("unsupported type for HISTOGRAM  node")
    fig = px.histogram(x=x, y=y)
    return DataContainer(type="plotly", fig=fig, x=x, y=y)
