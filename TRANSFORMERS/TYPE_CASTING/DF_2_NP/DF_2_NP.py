import pandas as pd
from flojoy import flojoy, DataContainer


@flojoy
def DF_2_NP(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
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
    dc_input = dc_inputs[0]
    if dc_input.type == "dataframe":
        df = dc_input.m
        df_to_numpy = df.to_numpy(dtype=object)

        return DataContainer(type="matrix", m=df_to_numpy)
    else:
        raise ValueError(
            f"unsupported DataContainer type passed for DF_2_NP : {dc_input.type}"
        )
