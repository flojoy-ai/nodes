from flojoy import flojoy, DataFrame, Matrix, Array
import pandas as pd
import numpy as np


@flojoy
def EXTRACT_COLUMNS(default: DataFrame | Matrix, columns: Array) -> DataFrame:
    """The EXTRACT_COLUMNS node takes an input dataframe/matrix and returns a dataframe/matrix with only the specified columns.

    Parameters
    ----------
    columns: list of str or list of int (supports python indexing)
        The columns to extract from the input dataframe.

    Returns
    -------
    DataFrame | Matrix
        The dataframe or matrix with only the specified columns.
    """
    if isinstance(default, DataFrame):
        df = default.m
        new_df = df[columns.unwrap()] if columns else df
        return DataFrame(df=new_df)
    else:
        matrix = default.m
        indices = np.array(columns.unwrap(), dtype=int)
        new_matrix = matrix[:, indices] if columns else matrix
        return Matrix(m=new_matrix)
