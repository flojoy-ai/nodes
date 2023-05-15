from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
import pandas as pd


@flojoy
def HISTOGRAM(dc_inputs: list[DataContainer], params: dict):
    """Node creates a Plotly Histogram visualization for a given input data container."""
    dc_input = dc_inputs[0]
    fig = go.Figure()
    match dc_input.type:
        case "ordered_pair":
            x = dc_input.x
            if isinstance(dc_input.x, dict):
                dict_keys = list(dc_input.x.keys())
                x = dc_input.x[dict_keys[0]]
            y = dc_input.y

            # Want to show the distribution of y values on the x axis
            fig.add_trace(go.Histogram(x=y))
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            for col in df.columns:
                fig.add_trace(go.Histogram(x=df[col], name=col))
            fig.update_layout(
                title="Histogram Plot", xaxis_title="Value", yaxis_title="Frequency"
            )
        case _:
            raise ValueError("unsupported DataContainer type for HISTOGRAM node")

    return DataContainer(type="plotly", fig=fig)
