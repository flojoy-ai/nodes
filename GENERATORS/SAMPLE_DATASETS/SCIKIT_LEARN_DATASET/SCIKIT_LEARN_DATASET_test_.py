# from flojoy import DataFrame
#
#
#
# # Tests that the function returns the expected DataFrame when called with the default dataset_key parameter
# def test_default_dataset_key(mock_flojoy_decorator):
#     import SCIKIT_LEARN_DATASET
#
#     result = SCIKIT_LEARN_DATASET.SCIKIT_LEARN_DATASET()
#     assert isinstance(result, DataFrame)
#     assert result.m.equals(data("iris"))
#
#
# # Tests that the function returns the expected DataFrame when called with the 'cars' dataset_key parameter
# def test_cars_dataset_key(mock_flojoy_decorator):
#     import SCIKIT_LEARN_DATASET
#
#     dataset_key = "cars"
#     result = SCIKIT_LEARN_DATASET.SCIKIT_LEARN_DATASET(dataset_key=dataset_key)
#     assert isinstance(result, DataFrame)
#     assert result.m.equals(data(dataset_key))
