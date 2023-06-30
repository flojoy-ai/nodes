import pandas as pd
import numpy as np
from flojoy import flojoy, DataContainer, DefaultParams

@flojoy
def NP_2_DF(default: DataContainer, default_parmas: DefaultParams) -> DataContainer:
    """
    Node to convert numpy array data into dataframe type data

    Parameters
    ----------
    None

    Returns
    -------
    dataframe
        Converted numpy array value from the input
    """
    dc_input = dc_inputs[0]
    match dc_input.type:
        case 'dataframe' | 'parametric_dataframe':
            return dc_input
        case 'ordered_pair' | 'parametric_ordered_pair':
            df = pd.DataFrame(dc_input.y)
            return DataContainer(type='dataframe', m=df)
        case 'ordered_triple' | 'parametric_ordered_triple':
            df = pd.DataFrame(dc_input.z)
            return DataContainer(type='dataframe', m=df)
        case 'matrix' | 'grayscale' | 'parametric_matrix' | 'parametric_grayscale':
            np_array = np.asarray(dc_input.m)
            df = pd.DataFrame(np_array)
            return DataContainer(type='dataframe', m=df)
        case 'image' | 'parametric_image':
            red = dc_input.r
            green = dc_input.g
            blue = dc_input.b
            if dc_input.a == None:
                merge = np.stack((red, green, blue), axis=2)
                merge = merge.reshape(-1, merge.shape[-1])
                df = pd.DataFrame(merge)
                return DataContainer(type='dataframe', m=df)
            else:
                alpha = dc_inputs[0].a
                merge = np.stack((red, green, blue, alpha), axis=2)
                merge = merge.reshape(-1, merge.shape[-1])
                df = pd.DataFrame(merge)
                return DataContainer(type='dataframe', m=df)
        case _:
            raise ValueError(f'unsupported DataContainer type passed for NP_2_DF : {dc_input.type}')