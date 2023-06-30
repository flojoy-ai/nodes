import traceback
from numpy import asarray
import pandas as pd
from flojoy import flojoy, DataContainer, DefaultParams

@flojoy
def MAT_2_DF(default: DataContainer, default_parmas: DefaultParams) -> DataContainer:
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
    dc_input = dc_inputs[0]
    if dc_input.type == 'matrix':
        np_data = dc_input.m
        np_array = asarray(np_data)
        df = pd.DataFrame(np_array)
        return DataContainer(type='dataframe', m=df)
    else:
        raise ValueError(f'unsupported DataContainer type passed for MAT_2_DF : {dc_input.type}')