from numpy import asarray
import pandas as pd
from flojoy import flojoy, Matrix, DataFrame


@flojoy
def MAT_2_DF(default: Matrix) -> DataFrame:
    """
    Node to convert matrix type data into dataframe type data.
    It takes one matrix type data and converts it to dataframe type data.

    Parameters
    ----------
    None

    Returns
    -------
    dataframe
        Converted matrix value from the input
    """

    np_data = default.m
    np_array = asarray(np_data)
    df = pd.DataFrame(np_array)

    return DataFrame(df=df)
