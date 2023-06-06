import pandas as pd
import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def NP_2_DF(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Node to convert numpy array data into dataframe type data
    """

    match (dc_inputs[0].type):
        case "dataframe":
            return dc_inputs[0]

        case "ordered_pair":
            df = pd.DataFrame(dc_inputs[0].y)
            return DataContainer(type="dataframe", m=df)

        case "ordered_triple":
            df = pd.DataFrame(dc_inputs[0].z)
            return DataContainer(type="dataframe", m=df)

        case "matrix" | "grayscale":
            npArray = np.asarray(dc_inputs[0].m)
            df = pd.DataFrame(npArray)
            return DataContainer(type="dataframe", m=df)

        case "image":
            red = dc_inputs[0].r
            green = dc_inputs[0].g
            blue = dc_inputs[0].b

            if dc_inputs[0].a == None:
                merge = np.stack((red, green, blue), axis=2)
                merge = merge.reshape(-1, merge.shape[-1])
                df = pd.DataFrame(merge)
                return DataContainer(
                    type="dataframe", m=df
                )
            else:
                alpha = dc_inputs[0].a
                merge = np.stack((red, green, blue, alpha), axis=2)
                merge = merge.reshape(-1, merge.shape[-1])
                df = pd.DataFrame(merge)
                return DataContainer(
                    type="dataframe", m=df
                )

        case "scalar":
            cToArray = np.asarray(dc_inputs[0].c)  # Not too sure about this part
            df = pd.DataFrame(cToArray)
            return DataContainer(type="dataframe", m=df)

        case "plotly":
            df = pd.DataFrame(dc_inputs[0].fig)  # Not too sure about this part
            return DataContainer(type="dataframe", m=df)
