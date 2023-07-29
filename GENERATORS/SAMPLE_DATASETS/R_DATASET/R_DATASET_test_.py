from rdatasets import data
from flojoy import DataFrame
import R_DATASET


# Tests that the function returns the expected DataFrame when called with the default dataset_key parameter
def test_default_dataset_key(mock_flojoy_decorator):
    result = R_DATASET.R_DATASET()
    assert isinstance(result, DataFrame)
    assert result.m.equals(data("iris"))


# Tests that the function returns the expected DataFrame when called with the 'cars' dataset_key parameter
def test_cars_dataset_key(mock_flojoy_decorator):
    dataset_key = "cars"
    result = R_DATASET.R_DATASET(dataset_key=dataset_key)
    assert isinstance(result, DataFrame)
    assert result.m.equals(data(dataset_key))
