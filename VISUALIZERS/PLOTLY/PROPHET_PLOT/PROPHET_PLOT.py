from flojoy import flojoy, DataContainer
from typing import Any, Dict, List
from prophet.plot import plot_plotly
from prophet.serialize import model_from_json


@flojoy
def PROPHET_PLOT(
    dc_inputs: List[DataContainer], params: Dict[str, Any]
) -> DataContainer:
    dc_input = dc_inputs[0]
    extra = dc_input.get("extra", None)
    if not extra or "prophet" not in extra:
        raise ValueError(
            "Prophet model must be available in DataContainer 'extra' key to plot"
        )

    node_name = __name__.split(".")[-1]

    model = model_from_json(extra["prophet"])
    if extra.get("run_forecast") is not None:
        forecast = dc_input.m
    else:
        future = model.make_future_dataframe(periods=params["periods"])
        forecast = model.predict(future)
    fig = plot_plotly(model, forecast)
    fig.update_layout(
        dict(title=node_name, autosize=True, template={}, height=None, width=None),
        overwrite=True,
    )

    return DataContainer(type="plotly", fig=fig)
