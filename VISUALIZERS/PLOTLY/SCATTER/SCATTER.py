import plotly.graph_objects as go
from flojoy import flojoy, DataContainer
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout
import numpy as np


@flojoy
def SCATTER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The SCATTER Node creates a Plotly Scatter visualization for a given input data container.

    Parameters:
    ----------
    None

    Supported DC types:
    -------------------
    `ordered_pair`, `dataframe`, `matrix`
    """
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)
    match dc_input.type:
        case "ordered_pair":
            x = dc_input.x
            if isinstance(dc_input.x, dict):
                dict_keys = list(dc_input.x.keys())
                x = dc_input.x[dict_keys[0]]
            y = dc_input.y
            fig.add_trace(go.Scatter(x=x, y=y, mode="markers", marker=dict(size=4)))
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            first_col = df.iloc[:, 0]
            is_timeseries = False
            if pd.api.types.is_datetime64_any_dtype(first_col):
                is_timeseries = True
            if is_timeseries:
                for col in df.columns:
                    if col != df.columns[0]:
                        fig.add_trace(
                            go.Scatter(x=first_col, y=df[col], mode="markers", name=col)
                        )
            else:
                for col in df.columns:
                    fig.add_trace(
                        go.Scatter(x=df.index, y=df[col], mode="markers", name=col)
                    )
        case "matrix":
            m: np.ndarray = dc_input.m

            num_rows, num_cols = m.shape

            x_ticks = np.arange(num_cols)

            for i in range(num_rows):
                fig.add_trace(
                    go.Scatter(x=x_ticks, y=m[i, :], name=f"Row {i+1}", mode="markers")
                )

            fig.update_layout(xaxis_title="Column", yaxis_title="Value")

        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )
    return DataContainer(type="plotly", fig=fig)
