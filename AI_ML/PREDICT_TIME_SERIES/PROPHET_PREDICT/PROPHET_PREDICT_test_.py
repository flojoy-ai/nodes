from functools import wraps
from unittest.mock import patch

import numpy as np
import pandas as pd
from flojoy import DataFrame
from prophet import Prophet
from prophet.serialize import model_from_json


# Python functions are decorated at module-loading time, So we'll need to patch our decorator
#  with a simple mock before loading the module.


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


# Patch the flojoy decorator that handles connecting our node to the App.
patch("flojoy.flojoy", mock_flojoy_decorator).start()

# After Patching the flojoy decorator, let's load the node under test.
import PROPHET_PREDICT


def test_PROPHET_PREDICT():
    # Generate random time series data
    start_date = pd.Timestamp("2023-01-01")
    end_date = pd.Timestamp("2023-07-20")
    num_days = (end_date - start_date).days + 1
    timestamps = pd.date_range(start=start_date, end=end_date, freq="D")
    data = np.random.randn(num_days)  # Random data points

    df = pd.DataFrame({"Timestamp": timestamps, "Data": data})
    dc = DataFrame(df=df)

    # node under test
    res = PROPHET_PREDICT.PROPHET_PREDICT([dc], {"run_forecast": True, "periods": 365})

    # Should get back a dataframe
    assert isinstance(res.m, pd.DataFrame)
    # Should get back extra with the model is json form and the original df
    extra = res.extra
    assert extra["run_forecast"] is True
    assert isinstance(extra["original"], pd.DataFrame)
    # This should be identical to the original df, all columns, all rows
    assert (extra["original"] == df).all().all()
    assert extra["prophet"] is not None
    assert isinstance(model_from_json(extra["prophet"]), Prophet)
