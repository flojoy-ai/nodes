import pandas as pd
from flojoy import flojoy, DataFrame, Matrix


@flojoy
def DF_2_NP(default: DataFrame) -> Matrix:
    """The DF_2_NP node takes one dataframe type data and converts it to a matrix type data.

    Inputs
    ------
    default : DataFrame
        The input dataframe to which we apply the conversion to.

    Returns
    -------
    Matrix
        The matrix result from the conversion of the input.
    """

    df = default.m
    df_to_numpy = df.to_numpy(dtype=object)

    return Matrix(m=df_to_numpy)
