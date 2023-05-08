from flojoy import flojoy, DataContainer
import plotly.graph_objects as go

@flojoy
def MULTIPLE_TIME_LINE(v, params):
    dc_input = v[0]
    if dc_input.type == 'ordered_pair':
        Numberoflines = dc_input.x                             #If dc.x is just a variable
        if isinstance(dc_input.x, dict):                       #If dc.x is a dict with many variables
            dict_keys = list(dc_input.x.keys())
            Numberoflines = dc_input.x[dict_keys[0]]           # Number of lines is de
        Measured_Values = dc_input.y
        y = dc_input.y
    else:
        raise ValueError('unsupported input type for LINE node')
    fig = go.Figure(data=go.Line(x=x, y=y, mode='markers'))
    return DataContainer(type='plotly', fig=fig, x=x, y=y)