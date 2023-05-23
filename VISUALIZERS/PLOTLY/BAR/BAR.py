from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import pandas as pd


@flojoy
def BAR(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly Bar visualization for a given input data container."""
    dc_input: DataContainer = dc_inputs[0]
    fig = go.Figure()
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
            fig.update_layout(
                title="Bar Plot", xaxis_title="X Axis", yaxis_title="Y Axis"
            )
        case _:
            raise ValueError("unsupported DataContainer type for BAR node")

    return DataContainer(type="plotly", fig=fig)
