import plotly.graph_objects as go
import plotly.express as px
from flojoy import DataContainer, flojoy, DefaultParams
from nodes.VISUALIZERS.template import plot_layout

@flojoy
def SCATTER3D(default: DataContainer, default_parmas: DefaultParams) -> DataContainer:
    """The SCATTER3D node creates a Plotly 3D Scatter visualization for a given input data container.

    Parameters:
    -----------
    None

    Supported DC types:
    -------------------
    `ordered_triple`, `dataframe`
    """
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split('.')[-1]
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)
    match dc_input.type:
        case 'ordered_triple':
            x = dc_input.x
            if isinstance(dc_input.x, dict):
                dict_keys = list(dc_input.x.keys())
                x = dc_input.x[dict_keys[0]]
            y = dc_input.y
            z = dc_input.z
            fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers'))
        case 'dataframe':
            df = dc_input.m
            if len(df.columns) < 3:
                raise ValueError('DataFrame must have at least 3 columns for x, y, and z coordinates.')
            x_column = df.columns[0]
            y_column = df.columns[1]
            z_column = df.columns[2]
            fig = px.scatter_3d(df, x=x_column, y=y_column, z=z_column, color=z_column)
        case _:
            raise ValueError(f'unsupported DataContainer type passed for {node_name}: {dc_input.type}')
    return DataContainer(type='plotly', fig=fig)