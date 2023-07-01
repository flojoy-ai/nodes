from flojoy import flojoy, DataContainer, DefaultParams
import pandas as pd
from typing import List, cast


@flojoy
def EXTRACT_COLUMNS(
    default: DataContainer,
    default_params: DefaultParams,
    columns: list[str | float | int] = [],
) -> DataContainer:
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
    dc = dc_inputs[0]
    if dc.type != "dataframe":
        raise ValueError(
            f"unsupported DataContainer type passed to EXTRACT_COLUMNS node: {dc.type}"
        )
    columns: List[str] = params.get("columns", None)
    df = cast(pd.DataFrame, dc.m)
    new_df = df[columns] if columns else df
    new_df = cast(pd.DataFrame, new_df)
    return DataContainer(type="dataframe", m=new_df)
