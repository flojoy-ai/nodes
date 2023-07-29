from flojoy import DataFrame


# Tests that the function loads the training set by default
def test_load_training_set_by_default(mock_flojoy_decorator):
    from TEXT_DATASET import TEXT_DATASET

    result = TEXT_DATASET()
    assert isinstance(result, DataFrame)
    assert len(result.m) == 11314
    assert set(result.m.columns) == {"Text", "Label"}
    assert set(result.m["Label"].unique()) == set(
        [
            "comp.graphics",
            "comp.os.ms-windows.misc",
            "comp.sys.ibm.pc.hardware",
            "comp.sys.mac.hardware",
            "comp.windows.x",
            "misc.forsale",
            "rec.autos",
            "rec.motorcycles",
            "rec.sport.baseball",
            "rec.sport.hockey",
            "sci.crypt",
            "sci.electronics",
            "sci.med",
            "sci.space",
            "soc.religion.christian",
            "talk.politics.guns",
            "talk.politics.mideast",
            "talk.politics.misc",
            "talk.religion.misc",
        ]
    )


# Tests that the function loads specific categories
def test_load_specific_categories(mock_flojoy_decorator):
    from TEXT_DATASET import TEXT_DATASET

    result = TEXT_DATASET(categories=["comp.graphics", "comp.os.ms-windows.misc"])
    assert isinstance(result, DataFrame)
    assert len(result.m) == 1189
    assert set(result.m.columns) == {"Text", "Label"}
    assert set(result.m["Label"].unique()) == set(
        ["comp.graphics", "comp.os.ms-windows.misc"]
    )


# Tests that the function loads an empty dataset
def test_load_empty_dataset(mock_flojoy_decorator):
    from TEXT_DATASET import TEXT_DATASET

    result = TEXT_DATASET(categories=["non-existent-category"])
    assert isinstance(result, DataFrame)
    assert len(result.m) == 0
    assert set(result.m.columns) == {"Text", "Label"}


# Tests that the function loads a dataset with all categories removed
def test_load_dataset_with_all_categories_removed(mock_flojoy_decorator):
    from TEXT_DATASET import TEXT_DATASET

    assert isinstance(result, DataFrame)
    result = TEXT_DATASET(remove_headers=True, remove_footers=True, remove_quotes=True)
    assert len(result.m) == 0
    assert set(result.m.columns) == {"Text", "Label"}
