import pandas as pd
from flojoy import flojoy, DataContainer, DataFrame, Matrix


@flojoy
def DF_2_NP(default: DataFrame) -> DataContainer:
    """
    Node to convert dataframe type data into matrix type data.
    It takes one dataframe type data and converts it to matrix type data.

    Parameters
    ----------
    None

    Returns
    -------
    numpy array
        Converted dataframe value from the input
    """

    df = default.m
    df_to_numpy = df.to_numpy(dtype=object)

    return Matrix(m=df_to_numpy)
