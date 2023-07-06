from flojoy import flojoy, DataFrame
import pandas as pd
from typing import cast


@flojoy
def EXTRACT_COLUMNS(default: DataFrame, columns: list[str] = "") -> DataFrame:
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
    df = cast(pd.DataFrame, default.df)
    new_df = df[columns] if columns else df
    new_df = cast(pd.DataFrame, new_df)

    return DataFrame(df=new_df)
