from flojoy import flojoy, DataFrame, Array
import pandas as pd
import numpy as np
from typing import cast


@flojoy
def EXTRACT_COLUMNS(default: DataFrame, columns: Array) -> DataFrame:
    """The EXTRACT_COLUMNS node takes an input dataframe and returns a dataframe with only the specified columns.

    Parameters
    ----------
    columns: list of str
        The columns to extract from the input dataframe.

    Returns
    -------
    dataframe
        The dataframe with only the specified columns.
    """
    df = cast(pd.DataFrame, default.m)
    new_df = df[columns.unwrap()] if columns else df
    new_df = cast(pd.DataFrame, new_df)
    return DataFrame(df=new_df)
