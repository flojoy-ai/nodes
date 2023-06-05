import traceback
from numpy import asarray
import pandas as pd
from flojoy import flojoy, DataContainer


@flojoy
def MAT_2_DF(dc_inputs : list[DataContainer(type="matrix")], params : dict) -> DataContainer:
    """
    Node to convert matrix type data into dataframe type data.
    It takes one matrix type data and converts it to dataframe type data.
    """
    try:
        npData = dc_inputs[0].m
        npArray = asarray(npData)
        df = pd.DataFrame(npArray)

        return DataContainer(type="dataframe", m=df)
    except Exception:
        print(traceback.format_exc())
        raise

