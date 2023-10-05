from flojoy import DataFrame
from sklearn.datasets import load_diabetes, load_iris


# Tests that the function returns the expected DataFrame when called with the default dataset_key parameter
def test_load_iris(mock_flojoy_decorator):
    import SCIKIT_LEARN_DATASET

    result = SCIKIT_LEARN_DATASET.SCIKIT_LEARN_DATASET(dataset_name="iris")
    assert isinstance(result, DataFrame)
    assert result.m.equals(load_iris(as_frame=True, return_X_y=True)[0])


# Tests that the function returns the expected DataFrame when called with the 'cars' dataset_key parameter
def test_load_diabetes(mock_flojoy_decorator):
    import SCIKIT_LEARN_DATASET

    result = SCIKIT_LEARN_DATASET.SCIKIT_LEARN_DATASET(dataset_name="diabetes")
    assert isinstance(result, DataFrame)
    assert result.m.equals(load_diabetes(as_frame=True, return_X_y=True)[0])
