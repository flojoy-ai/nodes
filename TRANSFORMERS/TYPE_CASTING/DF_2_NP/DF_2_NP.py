import traceback
from numpy import asmatrix, asarray
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
    if dc_inputs[0].type == "dataframe":
        pd_data = dc_inputs[0].m
        pd_to_numpy = pd.DataFrame(pd_data).to_numpy(dtype=object)
        pd_to_numpy = pd_to_numpy[:, :-1]
        # numpyMatrix = asmatrix(pdToNumpy)

        return DataContainer(type="matrix", m=pd_to_numpy)
    else:
        raise Exception("Invalid type")
