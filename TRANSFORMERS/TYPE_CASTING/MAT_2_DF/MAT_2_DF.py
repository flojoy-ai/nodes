import traceback
from numpy import asarray
import pandas as pd
from flojoy import flojoy, DataContainer


@flojoy
def MAT_2_DF(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
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
    if dc_inputs[0].type == "matrix":
        np_data = dc_inputs[0].m
        np_array = asarray(np_data)
        df = pd.DataFrame(np_array)

        return DataContainer(type="dataframe", m=df)
    else:
        raise Exception("Invalid type")
