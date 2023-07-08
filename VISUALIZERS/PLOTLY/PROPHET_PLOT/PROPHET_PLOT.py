from flojoy import flojoy, DataFrame, Plotly
from prophet.plot import plot_plotly
from prophet.serialize import model_from_json


@flojoy
def PROPHET_PLOT(default: DataFrame, periods: int = 365) -> Plotly:
    """The PROPHET_PLOT node plots forecasted trend of the time series data passed in

    This is the output plotly graph from the `plot_plotly` function
    from `prophet.plot`

    It expects as input the trained Prophet model from the PROPHET_PREDICT node. If
    `run_forecast` was True in that node, the forecasted dataframe will be available
    here as the `m` dc_input attribute. Otherwise, this will make the predictions on
    the raw dataframe (which will be the `m` attribute in that case). You can tell
    out if that forecasted dataframe is available via the `extra` field "run_forecast"
    of the dc_input (`dc_inputs[0].extra["run_forecast"]`)

    Parameters
    ----------
    periods : int
        The number of periods out to predict. Only used if the node passed into this
        node (ie PROPHET_PREDICT) did NOT return the forecast. If the forecast was
        included in the DataContainer, this param will be ignored.

        Default 365

    Returns
    -------
    DataContainer of type "plotly" with the figure containing the plotted components
    """
    extra = default.get("extra", None)
    if not extra or "prophet" not in extra:
        raise ValueError(
            "Prophet model must be available in DataContainer 'extra' key to plot"
        )

    node_name = __name__.split(".")[-1]

    model = model_from_json(extra["prophet"])
    if extra.get("run_forecast") is not None:
        forecast = default.m
    else:
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)
    fig = plot_plotly(model, forecast)
    fig.update_layout(
        dict(title=node_name, autosize=True, template={}, height=None, width=None),
        overwrite=True,
    )

    return Plotly(fig=fig)
