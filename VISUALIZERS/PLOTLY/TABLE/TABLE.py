from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def TABLE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly table visualization for a given input data container.

    Args:
    dc_inputs (list): A list of DataContainer object(s) containing the input data.
    params (dict): A dictionary containing the parameters needed for the visualization.

    Returns:
    DataContainer: A DataContainer object containing the generated visualization and the processed data.

    Raises:
    ValueError: If the input data container is not supported.
    """
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    if dc_input.type in ["dataframe", "plotly"]:
        df = pd.DataFrame(dc_input.m)
        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(values=list(df.columns), align="left"),
                    cells=dict(values=[df[col] for col in df.columns], align="left"),
                )
            ],
            layout=layout,
        )
        return DataContainer(type="plotly", fig=fig, m=df)
    else:
        raise ValueError(
            f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
        )
