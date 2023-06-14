from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def COMPOSITE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a combination of Plotly visualizations for a given input data container."""

    dc_input_1: DataContainer = dc_inputs[0]
    dc_input_2: DataContainer = dc_inputs[1]
    first_figure: str = params.get("first_figure")
    second_figure: str = params.get("second_figure")

    node_name: str = __name__.split(".")[-1]
    print("This is the node name: ", node_name)
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)

    match dc_input_1.type:
        case "ordered_pair":
            x = dc_input_1.x
            if isinstance(dc_input_1.x, dict):
                dict_keys = list(dc_input_1.x.keys())
                x = dc_input_1.x[dict_keys[0]]
            y = dc_input_1.y
            match first_figure:
                case "bar":
                    fig.add_trace(go.Bar(x=x, y=y))
                case "line":
                    fig.add_trace(go.Line(x=x, y=y, mode="lines"))
                case "histogram":
                    fig.add_trace(go.Histogram(x=y))
                case "scatter":
                    fig.add_trace(
                        go.Scatter(x=x, y=y, mode="markers", marker=dict(size=4))
                    )
        case "dataframe":
            df = pd.DataFrame(dc_input_1.m)
            for col in df.columns:
                match first_figure:
                    case "bar":
                        if df[col].dtype == "object":
                            counts = df[col].value_counts()
                            fig.add_trace(
                                go.Bar(
                                    x=counts.index.tolist(), y=counts.tolist(), name=col
                                )
                            )
                        else:
                            fig.add_trace(go.Bar(x=df.index, y=df[col], name=col))
                    case "line":
                        fig.add_trace(
                            go.Scatter(x=df.index, y=df[col], mode="lines", name=col)
                        )
                    case "histogram":
                        fig.add_trace(go.Histogram(x=df[col], name=col))
                    case "scatter":
                        fig.add_trace(
                            go.Scatter(x=df[col], y=df.index, mode="markers", name=col)
                        )

        case "matrix":
            if first_figure != "line":
                raise TypeError(
                    f"matrix DataContainer type only supports line visualizer"
                )

            y_columns: np.ndarray = dc_input_1.m
            for i, col in enumerate(y_columns.T):
                fig.add_trace(
                    go.Scatter(
                        x=np.arange(0, col.size),
                        y=col,
                        mode="lines",
                        name=i,
                    )
                )

        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input_1.type}"
            )

    match dc_input_2.type:
        case "ordered_pair":
            x = dc_input_2.x
            if isinstance(dc_input_2.x, dict):
                dict_keys = list(dc_input_2.x.keys())
                x = dc_input_2.x[dict_keys[0]]
            y = dc_input_2.y
            match second_figure:
                case "bar":
                    fig.add_trace(go.Bar(x=x, y=y))
                case "line":
                    fig.add_trace(go.Line(x=x, y=y, mode="lines"))
                case "histogram":
                    fig.add_trace(go.Histogram(x=x, y=y))
                case "scatter":
                    fig.add_trace(
                        go.Scatter(x=x, y=y, mode="markers", marker=dict(size=4))
                    )
        case "dataframe":
            df = pd.DataFrame(dc_input_2.m)
            for col in df.columns:
                match second_figure:
                    case "bar":
                        if df[col].dtype == "object":
                            counts = df[col].value_counts()
                            fig.add_trace(
                                go.Bar(
                                    x=counts.index.tolist(), y=counts.tolist(), name=col
                                )
                            )
                        else:
                            fig.add_trace(go.Bar(x=df.index, y=df[col], name=col))
                    case "line":
                        fig.add_trace(
                            go.Scatter(x=df.index, y=df[col], mode="lines", name=col)
                        )
                    case "histogram":
                        fig.add_trace(go.Histogram(x=df[col], name=col))
                    case "scatter":
                        fig.add_trace(
                            go.Scatter(x=df[col], y=df.index, mode="markers", name=col)
                        )

        case "matrix":
            if second_figure != "line":
                raise TypeError(
                    f"matrix DataContainer type only supports line visualizer"
                )

            y_columns: np.ndarray = dc_input_2.m
            for i, col in enumerate(y_columns.T):
                fig.add_trace(
                    go.Scatter(
                        x=np.arange(0, col.size),
                        y=col,
                        mode="lines",
                        name=i,
                    )
                )

        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input_2.type}"
            )

    fig.update_layout(dict(autosize=True, height=None, width=None))
    return DataContainer(type="plotly", fig=fig)
