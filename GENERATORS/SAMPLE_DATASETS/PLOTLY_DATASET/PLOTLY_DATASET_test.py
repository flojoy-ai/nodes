from plotly.express import data
import pandas as pd


# Tests that the function returns the expected DataFrame when called with the default dataset_key parameter
def test_default_dataset_key(mock_flojoy_decorator):
    result = PLOTLY_DATASET()
    assert isinstance(result, pd.DataFrame)
    assert result.equals(data.wind())


# Tests that the function returns the expected DataFrame when called with the 'iris' dataset_key parameter
def test_iris_dataset_key(mock_flojoy_decorator):
    result = PLOTLY_DATASET(dataset_key="iris")
    assert isinstance(result, pd.DataFrame)
    assert result.equals(data.iris())
