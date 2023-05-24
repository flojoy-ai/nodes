from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def BAR(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly Bar visualization for a given input data container."""
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
            for col in df.columns:
                if df[col].dtype == "object":
                    counts = df[col].value_counts()
                    fig.add_trace(
                        go.Bar(x=counts.index.tolist(), y=counts.tolist(), name=col)
                    )
                else:
                    fig.add_trace(go.Bar(x=df.index, y=df[col], name=col))
            fig.update_layout(xaxis_title="X Axis", yaxis_title="Y Axis")
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )

    return DataContainer(type="plotly", fig=fig)
