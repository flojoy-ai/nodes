from flojoy import flojoy, Dataframe
import pandas as pd


@flojoy
def ONE_HOT_ENCODING(
    default: Dataframe,
    categories: list[str | float | int] = [],
    columns: list[str | float | int] = [],
) -> Dataframe:
    """The ONE_HOT_ENCODING node creates a one hot encoding from a dataframe containing categorical features.

    Parameters
    ----------
    categories : list of str or list of int, optional
        A list of categories, can be used to generate a one hot encoding without having to pass a dataframe.
    columns: list of str, optional
        Specifies the columns to encode. By default, the node will encode all categorical columns.

    Returns
    -------
    matrix
        The one hot encoding of the input features.
    """
    if categories:
        data = pd.DataFrame({"category": categories})
        data["category"] = data["category"].astype("category")
        encoded = pd.get_dummies(data, dtype=int)
        return Dataframe(df=encoded)
    if columns:
        encoded = pd.get_dummies(default.m[columns])
    else:
        df = default.m
        cat_df = df.select_dtypes(include=["object", "category"])
        encoded = pd.get_dummies(cat_df, dtype=int)
    return Dataframe(df=encoded)
