from numpy import asarray
import pandas as pd
from flojoy import flojoy, Matrix, DataFrame


@flojoy
def MAT_2_DF(default: Matrix) -> DataFrame:
    """
    The MAT_2_DF node takes one matrix type data and converts it to a dataframe type data.

    Inputs
    ------
    default : Matrix
        The input Matrix to which we apply the conversion to.

    Returns
    -------
    DataFrame
        Converted matrix value from the input.
    """

    np_data = default.m
    np_array = asarray(np_data)
    df = pd.DataFrame(np_array)

    return DataFrame(df=df)
