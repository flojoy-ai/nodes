from flojoy import flojoy, DataContainer
from node_sdk.small_memory import SmallMemory
import plotly.graph_objects as go
from nodes.VISUALIZERS.template import plot_layout

MEMORY_KEY = "BIG_NUMBER_MEMORY_KEY"


@flojoy
def BIG_NUMBER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The BIG_NUMBER node generates a plotly figure displaying a big number with optional prefix and suffix.

    Parameters:
    -----------
    relative_delta: bool
        whether to show relative delta from last run along with big number
    suffix: str
        any suffix to show with big number
    prefix: str
        any prefix to show with big number
    title: str
        title of the plot. default `BIG_NUMBER`

    Supported DC types:
    -------------------
    `ordered_pair`
    """
    dc_input = dc_inputs[0]
    job_id = params["job_id"]
    relative_delta = params["relative_delta"]
    suffix = params["suffix"]
    prefix = params["prefix"]
    title = params["title"]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=title if title != "" else node_name)
    fig = go.Figure(layout=layout)
    match dc_input.type:
        case "ordered_pair":
            prev_num = SmallMemory().read_memory(job_id, MEMORY_KEY)
            big_num = dc_input.y[-1]
            val_format = ".1%" if relative_delta is True else ".1f"
            fig.add_trace(
                go.Indicator(
                    mode="number+delta",
                    value=int(float(big_num)),
                    domain={"y": [0, 1], "x": [0, 1]},
                    number={"prefix": prefix, "suffix": suffix},
                    delta=None
                    if prev_num is None
                    else {
                        "reference": int(float(prev_num)),
                        "relative": relative_delta,
                        "valueformat": val_format,
                    },
                )
            )
            SmallMemory().write_to_memory(job_id, MEMORY_KEY, big_num)
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )
    return DataContainer(type="plotly", fig=fig)
