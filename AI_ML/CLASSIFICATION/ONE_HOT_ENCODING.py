from flojoy import flojoy, DataContainer
import pandas as pd


@flojoy
def ONE_HOT_ENCODING(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The ONE_HOT_ENCODING node creates a one hot encoding from a list of categorical features.
    Parameters
    ----------
    categories : array-like of str | int, optional
    columns: list of str

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
    if len(columns) == 0:
        columns = None

    if categories:
        data = pd.DataFrame({"category": categories})
        # Force pandas to treat the column as categorical
        data["category"] = data["category"].astype("category")
        encoded = pd.get_dummies(data, dtype=int)

        return DataContainer(type="dataframe", m=encoded)

    if not dc:
        raise ValueError(f"ONE_HOT_ENCODING node did not receive input DataContainer")

    encoded = pd.get_dummies(dc.m, columns=columns, dtype=int)
    return DataContainer(type="dataframe", m=encoded)
