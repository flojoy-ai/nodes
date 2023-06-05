import traceback
from numpy import asmatrix, asarray
import pandas as pd
from flojoy import flojoy, DataContainer


@flojoy
def DF_2_NP(
    dc_inputs: list[DataContainer], params: dict
) -> DataContainer:
    """
    Node to convert dataframe type data into matrix type data.
    It takes one dataframe type data and converts it to matrix type data.
    """
    try:
        pdData = dc_inputs[0].m
        print("----------------------Type of the Value: ", type(pdData))
        #pdData = pd.concat(pd.DataFrame(pdData), axis=1)
        pdToNumpy = pd.DataFrame(pdData).to_numpy(dtype=object)
        print("----------------------Type of the Value: ", pdToNumpy)
        print("----------------------Type of the Value: ", pdToNumpy[:,:-1])
        pdToNumpy = pdToNumpy[:,:-1]
        #numpyMatrix = asmatrix(pdToNumpy)
        #print("----------------------Type of the Value: ", type(pdToNumpy))

        return DataContainer(type="matrix", m=pdToNumpy)
        # print("-----------------------------------------------------: ", pdToNumpy.shape)
        # return dc_inputs[0]
    except Exception:
        print(traceback.format_exc())
        raise
