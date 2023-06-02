import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def DF_2_NP(dc_input: DataContainer(type="dataframe")) -> DataContainer:
    """
    Node to convert dataframe type data into matrix type data
    """
    if dc_input.type == "dataframe":
        pdToNumpy = dc_input.to_numpy
        numpyMatrix = np.asmatrix(pdToNumpy)

        return DataContainer(m=numpyMatrix)
    else:
        print("Invalid type of DataContainer")