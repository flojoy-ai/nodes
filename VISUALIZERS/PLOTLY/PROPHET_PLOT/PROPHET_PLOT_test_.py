import pytest
import os
import pandas as pd
from flojoy import DataFrame, DataContainer
from plotly.graph_objs import Figure

@pytest.fixture
def mock_prophet_model_json():
    with open(os.path.join(os.path.dirname(__file__), "mock_prophet_model.json"), "r") as f:
        return f.read()

@pytest.fixture
def mock_prophet_output_dataframe():
    return pd.read_parquet(os.path.join(os.path.dirname(__file__), "mock_prophet_output_dataframe.parquet"))



def test_PROPHET_PLOT(mock_flojoy_decorator, mock_prophet_output_dataframe, mock_prophet_model_json):
    
    import PROPHET_PLOT

    default = DataFrame(df=mock_prophet_output_dataframe)
    for run_forecast in [True, False]:
        prophet_data = DataContainer(
            extra={"run_forecast": run_forecast, "prophet": mock_prophet_model_json}
        )
        res = PROPHET_PLOT.PROPHET_PLOT(default=default, data=prophet_data)
        # Should get back a plotly figure
        assert res.type == "plotly"
        assert isinstance(res.fig, Figure)
        assert res.fig.layout.title.text == "PROPHET_PLOT"