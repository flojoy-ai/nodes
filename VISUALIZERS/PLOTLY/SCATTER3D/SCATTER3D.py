import plotly.graph_objects as go
from flojoy import DataContainer, flojoy
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def SCATTER3D(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    if dc_input.type == "ordered_triple":
        x = dc_input.x
        if isinstance(dc_input.x, dict):
            dict_keys = list(dc_input.x.keys())
            x = dc_input.x[dict_keys[0]]
        y = dc_input.y
        z = dc_input.z
    else:
        raise ValueError(
            f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
        )
    layout = plot_layout(title=node_name)
    fig = go.Figure(data=go.Scatter3d(x=x, y=y, z=z, mode="markers"), layout=layout)

    return DataContainer(type="plotly", fig=fig, x=x, y=y, z=z)
