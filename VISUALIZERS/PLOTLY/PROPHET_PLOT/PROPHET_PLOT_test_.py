from functools import wraps
from unittest.mock import patch

import numpy as np
import pandas as pd
from flojoy import DataContainer
from plotly.graph_objs import Figure
from prophet import Prophet
from prophet.serialize import model_from_json, model_to_json


# Python functions are decorated at module-loading time, So we'll need to patch our decorator
#  with a simple mock ,before loading the module.


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


# Patch the flojoy decorator that handles connecting our node to the App.
patch("flojoy.flojoy", mock_flojoy_decorator).start()

# After Patching the flojoy decorator, let's load the node under test.
import PROPHET_PLOT


def test_PROPHET_PLOT():
    # Generate random time series data
    start_date = pd.Timestamp("2023-01-01")
    end_date = pd.Timestamp("2023-07-20")
    num_days = (end_date - start_date).days + 1
    timestamps = pd.date_range(start=start_date, end=end_date, freq="D")
    data = np.random.randn(num_days)  # Random data points
    df = pd.DataFrame({"ds": timestamps, "y": data})
    # Run prediction
    prophet = Prophet()
    prophet.fit(df)
    future = prophet.make_future_dataframe(periods=365)
    forecast = prophet.predict(future)

    model = model_to_json(prophet)
    dc = DataContainer(
        type="dataframe", m=forecast, extra={"run_forecast": True, "prophet": model}
    )

    # node under test
    res = PROPHET_PLOT.PROPHET_PLOT([dc], {})

    # Should get back a plotly figure
    assert res.type == "plotly"
    assert isinstance(res.fig, Figure)
    assert res.fig.layout.title.text == "PROPHET_PLOT"
