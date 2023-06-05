import traceback
from numpy import asmatrix
from pandas import to_numpy
from flojoy import flojoy, DataContainer


@flojoy
def DF_2_NP(
    dc_inputs: list[DataContainer(type="dataframe")], params: dict
) -> DataContainer:
    """
    Node to convert dataframe type data into matrix type data.
    It takes one dataframe type data and converts it to matrix type data.
    """
    try:
        pdData = dc_inputs[0].m
        pdToNumpy = pdData.to_numpy()
        numpyMatrix = asmatrix(pdToNumpy)

        return DataContainer(type="matrix", m=numpyMatrix)
    except Exception:
        print(traceback.format_exc())
        raise
