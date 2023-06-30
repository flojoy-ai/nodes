from flojoy import flojoy, DataFrame, Plotly, DefaultParams
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout

@flojoy(node_type='PLOTLY_VISOR')
def TABLE(default: DataFrame) -> Plotly:
    """Node creates a Plotly table visualization for a given input data container.

    Args:
    dc_inputs (list): A list of DataContainer object(s) containing the input data.
    params (dict): A dictionary containing the parameters needed for the visualization.

    Returns:
    DataContainer: A DataContainer object containing the generated visualization and the processed data.

    Raises:
    ValueError: If the input data container is not supported.
    """
    layout = plot_layout(title='TABLE')
    if not isinstance(default, DataFrame):
        raise ValueError(f'unsupported DataContainer type passed for TABLE: {default.type}')
    df = default.m
    fig = go.Figure(data=[go.Table(header=dict(values=list(df.columns), align='left'), cells=dict(values=[df[col] for col in df.columns], align='left'))], layout=layout)
    return Plotly(fig=fig)