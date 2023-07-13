from flojoy import flojoy, Matrix, DataFrame, Array

from typing import Optional
import pandas as pd


@flojoy
def ONE_HOT_ENCODING(
    default: DataFrame,
    columns: Optional[Array] = None,
) -> DataFrame:
    """The ONE_HOT_ENCODING node creates a one hot encoding from a dataframe containing categorical features.

    Parameters
    ----------
    columns: list of str, optional
        Specifies the columns to encode. By default, the node will encode all categorical columns.

    Returns
    -------
    matrix
        The one hot encoding of the input features.
    """

    df = default.m
    if columns and columns.unwrap():
        encoded = pd.get_dummies(df, columns=columns.unwrap())

    else:
        cat_df = df.select_dtypes(include=["object", "category"]).columns.to_list()
        encoded = pd.get_dummies(df, columns=cat_df)

    return DataFrame(df=encoded)
