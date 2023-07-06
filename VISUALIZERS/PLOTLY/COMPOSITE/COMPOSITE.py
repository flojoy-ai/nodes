from flojoy import flojoy, Plotly, DataFrame, OrderedPair, OrderedTriple, Matrix
from typing import Literal
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def COMPOSITE(
    figure1: DataFrame | OrderedPair  | OrderedTriple | Matrix,
    figure2: DataFrame | OrderedPair  | OrderedTriple | Matrix,
    first_figure: Literal["bar", "line", "histogram", "scatter"] = "line",
    second_figure: Literal["bar", "line", "histogram", "scatter"] = "line",
    ) -> Plotly:
    """The COMPOSITE node creates a combination of Plotly visualizations for a given input data container.

    Parameters
    ----------
    first_figure: 'bar' | 'line' | 'histogram' | 'scatter'
    second_figure: 'bar' | 'line' | 'histogram' | 'scatter'

    Supported DC types:
    ----------------
    `OrderedPair`, `DataFrame` (including timeseries), `OrderedTriple`, `Matrix`

    """
    node_name: str = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)

    match figure1.type:
        case "ordered_pair":
            x = figure1.x
            if isinstance(figure1.x, dict):
                dict_keys = list(figure1.x.keys())
                x = figure1.x[dict_keys[0]]
            y = figure1.y
            match first_figure:
                case "bar":
                    fig.add_trace(go.Bar(x=x, y=y))
                case "line":
                    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
                case "histogram":
                    fig.add_trace(go.Histogram(x=y))
                case "scatter":
                    fig.add_trace(
                        go.Scatter(x=x, y=y, mode="markers", marker=dict(size=4))
                    )

        case "ordered_triple":
            x = figure1.x
            y = figure1.y
            z = figure1.z
            match first_figure:
                case "bar":
                    fig.add_trace(go.Bar(x=x, y=y, z=z))
                case "line":
                    fig.add_trace(go.Scatter(x=x, y=y, z=z, mode="lines"))

        case "dataframe":
            df = pd.DataFrame(figure1.m)
            first_col = df.iloc[:, 0]
            is_timeseries = False
            if pd.api.types.is_datetime64_any_dtype(first_col):
                is_timeseries = True

            match first_figure:
                case "bar":
                    if is_timeseries:
                        for col in df.columns:
                            if col != df.columns[0]:
                                fig.add_trace(
                                    go.Bar(y=df[col].values, x=first_col, name=col)
                                )
                        fig.update_layout(xaxis_title=df.columns[0])
                    else:
                        for col in df.columns:
                            if df[col].dtype == "object":
                                counts = df[col].value_counts()
                                fig.add_trace(
                                    go.Bar(
                                        x=counts.index.tolist(),
                                        y=counts.tolist(),
                                        name=col,
                                    )
                                )
                            else:
                                fig.add_trace(go.Bar(x=df.index, y=df[col], name=col))
                        fig.update_layout(xaxis_title="DF index", yaxis_title="Y Axis")
                case "line":
                    if is_timeseries:
                        for col in df.columns:
                            if col != df.columns[0]:
                                fig.add_trace(
                                    go.Scatter(
                                        y=df[col].values,
                                        x=first_col,
                                        mode="lines",
                                        name=col,
                                    )
                                )
                    else:
                        for col in df.columns:
                            fig.add_trace(
                                go.Scatter(
                                    y=df[col].values,
                                    x=df.index,
                                    mode="lines",
                                    name=col,
                                )
                            )
                case "histogram":
                    for col in df.columns:
                        fig.add_trace(go.Histogram(x=df[col], name=col))
                    fig.update_layout(xaxis_title="Value", yaxis_title="Frequency")
                case "scatter":
                    if is_timeseries:
                        for col in df.columns:
                            if col != df.columns[0]:
                                fig.add_trace(
                                    go.Scatter(
                                        x=first_col, y=df[col], mode="markers", name=col
                                    )
                                )
                    else:
                        for col in df.columns:
                            fig.add_trace(
                                go.Scatter(
                                    x=df.index, y=df[col], mode="markers", name=col
                                )
                            )

        case "matrix":
            m: np.ndarray = figure1.m
            num_rows, num_cols = m.shape
            x_ticks = np.arange(num_cols)

            match first_figure:
                case "bar":
                    for i in range(num_rows):
                        fig.add_trace(go.Bar(x=x_ticks, y=m[i, :], name=f"Row {i+1}"))
                        fig.update_layout(xaxis_title="Column", yaxis_title="Value")
                case "line":
                    for i in range(num_rows):
                        fig.add_trace(
                            go.Scatter(
                                x=x_ticks, y=m[i, :], name=f"Row {i+1}", mode="lines"
                            )
                        )
                        fig.update_layout(xaxis_title="Column", yaxis_title="Value")
                case "histogram":
                    histogram_trace = go.Histogram(x=m.flatten())
                    fig.add_trace(go.Histogram(histogram_trace))

        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {figure1.type}"
            )

    match figure2.type:
        case "ordered_pair":
            x = figure2.x
            if isinstance(figure2.x, dict):
                dict_keys = list(figure2.x.keys())
                x = figure2.x[dict_keys[0]]
            y = figure2.y
            match second_figure:
                case "bar":
                    fig.add_trace(go.Bar(x=x, y=y))
                case "line":
                    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
                case "histogram":
                    fig.add_trace(go.Histogram(x=y))
                case "scatter":
                    fig.add_trace(
                        go.Scatter(x=x, y=y, mode="markers", marker=dict(size=4))
                    )

        case "ordered_triple":
            x = figure2.x
            y = figure2.y
            z = figure2.z
            match second_figure:
                case "bar":
                    fig.add_trace(go.Bar(x=x, y=y, z=z))
                case "line":
                    fig.add_trace(go.Scatter(x=x, y=y, z=z, mode="lines"))

        case "dataframe":
            df = pd.DataFrame(figure2.m)
            first_col = df.iloc[:, 0]
            is_timeseries = False
            if pd.api.types.is_datetime64_any_dtype(first_col):
                is_timeseries = True

            match second_figure:
                case "bar":
                    if is_timeseries:
                        for col in df.columns:
                            if col != df.columns[0]:
                                fig.add_trace(
                                    go.Bar(y=df[col].values, x=first_col, name=col)
                                )
                        fig.update_layout(xaxis_title=df.columns[0])
                    else:
                        for col in df.columns:
                            if df[col].dtype == "object":
                                counts = df[col].value_counts()
                                fig.add_trace(
                                    go.Bar(
                                        x=counts.index.tolist(),
                                        y=counts.tolist(),
                                        name=col,
                                    )
                                )
                            else:
                                fig.add_trace(go.Bar(x=df.index, y=df[col], name=col))
                        fig.update_layout(xaxis_title="DF index", yaxis_title="Y Axis")
                case "line":
                    if is_timeseries:
                        for col in df.columns:
                            if col != df.columns[0]:
                                fig.add_trace(
                                    go.Scatter(
                                        y=df[col].values,
                                        x=first_col,
                                        mode="lines",
                                        name=col,
                                    )
                                )
                    else:
                        for col in df.columns:
                            fig.add_trace(
                                go.Scatter(
                                    y=df[col].values,
                                    x=df.index,
                                    mode="lines",
                                    name=col,
                                )
                            )
                case "histogram":
                    for col in df.columns:
                        fig.add_trace(go.Histogram(x=df[col], name=col))
                    fig.update_layout(xaxis_title="Value", yaxis_title="Frequency")
                case "scatter":
                    if is_timeseries:
                        for col in df.columns:
                            if col != df.columns[0]:
                                fig.add_trace(
                                    go.Scatter(
                                        x=first_col, y=df[col], mode="markers", name=col
                                    )
                                )
                    else:
                        for col in df.columns:
                            fig.add_trace(
                                go.Scatter(
                                    x=df.index, y=df[col], mode="markers", name=col
                                )
                            )

        case "matrix":
            m: np.ndarray = figure2.m
            num_rows, num_cols = m.shape
            x_ticks = np.arange(num_cols)

            match second_figure:
                case "bar":
                    for i in range(num_rows):
                        fig.add_trace(go.Bar(x=x_ticks, y=m[i, :], name=f"Row {i+1}"))
                        fig.update_layout(xaxis_title="Column", yaxis_title="Value")
                case "line":
                    for i in range(num_rows):
                        fig.add_trace(
                            go.Scatter(
                                x=x_ticks, y=m[i, :], name=f"Row {i+1}", mode="lines"
                            )
                        )
                        fig.update_layout(xaxis_title="Column", yaxis_title="Value")
                case "histogram":
                    histogram_trace = go.Histogram(x=m.flatten())
                    fig.add_trace(go.Histogram(histogram_trace))

        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {figure2.type}"
            )

    fig.update_layout(dict(autosize=True, height=None, width=None))
    return Plotly(fig=fig)
