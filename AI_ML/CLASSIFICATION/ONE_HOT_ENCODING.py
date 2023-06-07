from flojoy import flojoy, DataContainer
import pandas as pd


@flojoy
def ONE_HOT_ENCODING(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The ONE_HOT_ENCODING node creates a one hot encoding from a list of categorical features.
    The `categories` parameter can be used to generate a one hot encoding without having to pass a dataframe.
    By default, all categorical columns in the input dataframe will be encoded. The `columns`
    parameter can be used to specify the columns to encode.

    Parameters
    ----------
    categories : list of str or list of int, optional
    columns: list of str, optional

    Returns
    -------
    matrix
        The one hot encoding of the input features.
    """

    dc = dc_inputs[0] if len(dc_inputs) > 0 else None

    if dc is not None and dc.type != "dataframe":
        raise ValueError(
            f"unsupported DataContainer type passed to ONE_HOT_ENCODING node: '{dc.type}'"
        )

    categories = params.get("categories", [])
    columns = params.get("columns", [])

    if categories:
        data = pd.DataFrame({"category": categories})
        # Force pandas to treat the column as categorical
        data["category"] = data["category"].astype("category")
        encoded = pd.get_dummies(data, dtype=int)

        return DataContainer(type="dataframe", m=encoded)

    if not dc:
        raise ValueError(f"ONE_HOT_ENCODING node did not receive input DataContainer")

    if columns:
        encoded = pd.get_dummies(dc.m[columns])
    else:
        cat_df = dc.m.select_dtypes(include=["object", "category"])
        encoded = pd.get_dummies(cat_df, dtype=int)

    return DataContainer(type="dataframe", m=encoded)
