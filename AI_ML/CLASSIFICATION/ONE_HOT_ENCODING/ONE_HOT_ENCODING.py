from flojoy import flojoy, Matrix, DataFrame, Array

from typing import Optional
import pandas as pd


@flojoy
def ONE_HOT_ENCODING(
    default: DataFrame,
    categories: Optional[Array] = None,
    columns: Optional[Array] = None,
) -> DataFrame:
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

    if categories.unwrap() != []:
        data = pd.DataFrame.from_dict({"category": categories.unwrap()})
        # Force pandas to treat the column as categorical
        data["category"] = data["category"].astype("category")
        encoded = pd.get_dummies(data, columns=["category"])
        return DataFrame(df=encoded)

    if columns:
        encoded = pd.get_dummies(default.m, columns=columns.unwrap())
    else:
        df = default.m
        cat_df = df.select_dtypes(include=["object", "category"]).columns.to_list()
        encoded = pd.get_dummies(cat_df)
    return DataFrame(df=encoded)
