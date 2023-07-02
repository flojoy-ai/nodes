from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout
import numpy as np


@flojoy
def BAR(
    default: DataContainer,
) -> DataContainer:
    """The BAR node creates a Plotly Bar visualization for a given input data container.

    Parameters
    ----------
    None

    Supported DC types:
    ----------------
    `ordered_pair`, `dataframe` (including timeseries), `matrix`
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
            fig.add_trace(go.Bar(x=x, y=y))
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            first_col = df.iloc[:, 0]
            is_timeseries = False
            if pd.api.types.is_datetime64_any_dtype(first_col):
                is_timeseries = True
            if is_timeseries:
                for col in df.columns:
                    if col != df.columns[0]:
                        fig.add_trace(go.Bar(y=df[col].values, x=first_col, name=col))
                fig.update_layout(xaxis_title=df.columns[0])
            else:
                for col in df.columns:
                    if df[col].dtype == "object":
                        counts = df[col].value_counts()
                        fig.add_trace(
                            go.Bar(x=counts.index.tolist(), y=counts.tolist(), name=col)
                        )
                    else:
                        fig.add_trace(go.Bar(x=df.index, y=df[col], name=col))
                fig.update_layout(xaxis_title="DF index", yaxis_title="Y Axis")
        case "matrix":
            m: np.ndarray = dc_input.m
            (num_rows, num_cols) = m.shape
            x_ticks = np.arange(num_cols)
            for i in range(num_rows):
                fig.add_trace(go.Bar(x=x_ticks, y=m[i, :], name=f"Row {i + 1}"))
            fig.update_layout(xaxis_title="Column", yaxis_title="Value")
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )
    return DataContainer(type="plotly", fig=fig)
