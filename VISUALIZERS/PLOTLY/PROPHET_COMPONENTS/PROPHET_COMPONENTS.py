from nodes.VISUALIZERS.template import plot_layout
from flojoy import flojoy, DataContainer
from typing import Any, Dict, List


@flojoy
def PROPHET_COMPONENTS(dc: List[DataContainer], params: Dict[str, Any]) -> DataContainer:
    try:
        from prophet import Prophet
        from prophet.plot import plot_components_plotly
        from prophet.serialize import model_from_json
    except ImportError:
        raise Exception("You must install prophet for this node")
    if not len(dc):
        raise ValueError("Must receive a prophet model to plot forecast")
    if "prophet" not in dc[0].extra:
        raise ValueError("Prophet model must be available to plot")
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)

    model = model_from_json(dc[0].extra["prophet"])
    if dc[0].extra.get("forecast") is not None:
        forecast = dc[0].extra.get("forecast")
    else:
        future = model.make_future_dataframe(periods=params["periods"])
        forecast = model.predict(future)
    fig = plot_components_plotly(model, forecast)
    fig.layout = layout
    fig.write_image("/tmp/components.jpeg")

    return DataContainer(
        type='plotly',
        fig=fig
    )
