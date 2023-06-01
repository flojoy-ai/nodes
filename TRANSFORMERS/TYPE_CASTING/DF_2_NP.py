import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def DF_2_NP(dc_input: DataContainer):
    if dc_input.type == "dataframe":
        pdToNumpy = dc_input.to_numpy
        numpyMatrix = np.asmatrix(pdToNumpy)
        dc_input.set_data(numpyMatrix)
