from flojoy import flojoy, DataFrame
from typing import Optional
import pandas as pd


@flojoy
def ONE_HOT_ENCODING(
    data: DataFrame,
    feature_col: Optional[DataFrame] = None,
) -> DataFrame:
    """
    The ONE_HOT_ENCODING node creates a one hot encoding from a dataframe and columns dataframe containing categorical features.

    Returns
    -------
    DataFrame
        The one hot encoding of the input features.
    """

    df = data.m
    if feature_col:
        encoded = pd.get_dummies(df, columns=feature_col.m.columns.to_list())

    else:
        cat_df = df.select_dtypes(include=["object", "category"]).columns.to_list()
        encoded = pd.get_dummies(df, columns=cat_df)

    return DataFrame(df=encoded)
