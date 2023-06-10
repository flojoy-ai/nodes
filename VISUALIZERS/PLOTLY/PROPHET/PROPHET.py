import numpy as np
import pandas as pd
from flojoy import flojoy, DataContainer
from typing import Any, Dict, List

@flojoy
def PROPHET(dc: List[DataContainer], params: Dict[str, Any]) -> DataContainer:
    try:
        from prophet import Prophet
        from prophet.plot import plot_plotly
    except ImportError:
        raise Exception("You must install Prohet for this node")

    ts = dc[0].x
    y = dc[0].y
    df = pd.DataFrame(dict(ds=ts, y=y))
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=params["periods"])
    forecast = model.predict(future)
    fig = plot_plotly(model, forecast)

    return DataContainer(
        type='plotly',
        fig=fig
    )
