from flojoy import flojoy, OrderedPair, DataFrame, Matrix, Plotly
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout
import numpy as np


@flojoy
def BAR(default: OrderedPair | DataFrame | Matrix) -> Plotly:
    """The BAR node creates a Plotly Bar visualization for a given input data container.

    Parameters
    ----------
    None

    Supported DC types:
    ----------------
    `ordered_pair`, `dataframe` (including timeseries), `matrix`
    """

    layout = plot_layout(title="BAR")
    fig = go.Figure(layout=layout)

    if isinstance(default, OrderedPair):
        x = default.x
        if isinstance(default.x, dict):
            dict_keys = list(default.x.keys())
            x = default.x[dict_keys[0]]
        y = default.y
        fig.add_trace(go.Bar(x=x, y=y))
    elif isinstance(default, DataFrame):
        df = default.m
        first_col = df.iloc[:, 0]
        is_timeseries = False
        if pd.api.types.is_datetime64_any_dtype(first_col):
            is_timeseries = True
        if is_timeseries:
            for col in df.columns:
                if col != df.columns[0]:
                    fig.add_trace(
                        go.Bar(
                            y=df[col].values,
                            x=first_col,
                            name=col,
                        )
                    )
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

    else:
        m = default.m

        num_rows, num_cols = m.shape

        x_ticks = np.arange(num_cols)

        for i in range(num_rows):
            fig.add_trace(go.Bar(x=x_ticks, y=m[i, :], name=f"Row {i+1}"))

        fig.update_layout(xaxis_title="Column", yaxis_title="Value")

    return Plotly(fig=fig)
