import pandas as pd
import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def NP_2_DF(dc_inputs : list[DataContainer], params : dict) -> DataContainer:
    """
    Node to convert numpy array data into dataframe type data
    """

    match (dc_inputs[0].type):
        case "ordered_pair":   
            df = pd.DataFrame(dc_inputs[0].y)
            return DataContainer(type="dataframe", x=dc_inputs[0].x, y=df)
        case "ordered_triple":
            df1 = pd.DataFrame(dc_inputs[0].y)
            df2 = pd.DataFrame(dc_inputs[0].z)
            return DataContainer(type="dataframe", x=dc_inputs[0].x, y=df1, z=df2)
        case "matrix" | "grayscale":
            npArray = np.asarray(dc_inputs[0].m)
            df = pd.DataFrame(npArray)
            return DataContainer(type="dataframe", m=df)
        case "dataframe" | "image" | "scalar" | "plotly":
            pass

