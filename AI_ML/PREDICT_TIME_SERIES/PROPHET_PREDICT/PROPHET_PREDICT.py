import pandas as pd
from flojoy import flojoy, DataContainer
from typing import Any, Dict, List


@flojoy
def PROPHET_PREDICT(dc: List[DataContainer], params: Dict[str, Any]) -> DataContainer:
    try:
        from prophet import Prophet
        from prophet.plot import plot_plotly
        from prophet.serialize import model_to_json
    except ImportError:
        raise Exception("You must install prophet for this node")

    df = pd.DataFrame(dict(ds=dc[0].x, y=dc[0].y))
    model = Prophet()
    model.fit(df)
    extra = {"prophet": model_to_json(model)}

    if params.get("run_forecast"):
        future = model.make_future_dataframe(periods=params["periods"])
        forecast = model.predict(future)
        extra["forecast"] = forecast
    return DataContainer(
        type='dataframe',
        m=df,
        extra=extra,
    )
