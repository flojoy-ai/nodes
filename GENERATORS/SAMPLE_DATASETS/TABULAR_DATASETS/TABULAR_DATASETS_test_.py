

def test_tabular_dataset(mock_flojoy_decorator):
    import TABULAR_DATASETS


    DATASETS_MAP = {
        "Iris": {
            "n_rows": 150,
            "n_cols": 5,
        },
        "Diabetes": {
            "n_rows": 442,
            "n_cols": 11,
        },
        "Digits": {
            "n_rows": 1797,
            "n_cols": 65,
        },
        "Wine": {
            "n_rows": 178,
            "n_cols": 14,
        },
        "Linnerud": {
            "n_rows": 20,
            "n_cols": 6,
        },
        "Breast Cancer": {
            "n_rows": 569,
            "n_cols": 31,
        }
    }

    for ds_name, dims in DATASETS_MAP.items():
        ds = TABULAR_DATASETS.TABULAR_DATASETS(dataset=ds_name)
        # Checks that the dataset has the correct number of rows and columns
        assert ds.m.shape == (dims["n_rows"], dims["n_cols"])

    
