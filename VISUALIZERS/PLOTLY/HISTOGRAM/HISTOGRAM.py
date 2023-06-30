from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout
import numpy as np


@flojoy
def HISTOGRAM(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The HISTOGRAM node creates a Plotly Histogram visualization for a given
    input data container.

    Parameters:
    -----------
    None

    Supported DC types:
    ------------------
    `ordered_pair`, `dataframe`, `matrix`

    """
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)
    match dc_input.type:
        case "ordered_pair":
            y = dc_input.y
            fig.add_trace(go.Histogram(x=y))
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            for col in df.columns:
                fig.add_trace(go.Histogram(x=df[col], name=col))
            fig.update_layout(xaxis_title="Value", yaxis_title="Frequency")
        case "matrix":
            m: np.ndarray = dc_input.m

            flattened_matrix = m.flatten()

            histogram_trace = go.Histogram(x=flattened_matrix)

            fig = fig.add_trace(histogram_trace)

        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )
    return DataContainer(type="plotly", fig=fig)
