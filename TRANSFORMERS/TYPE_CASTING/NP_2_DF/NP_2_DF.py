import pandas as pd
import numpy as np
from flojoy import (
    flojoy,
    DataContainer,
    DataFrame,
    OrderedPair,
    OrderedTriple,
    Matrix,
    Grayscale,
    Image,
    ParametricDataFrame,
    ParametricOrderedPair,
    ParametricOrderedTriple,
    ParametricImage,
    ParametricGrayscale,
    ParametricMatrix,
)


@flojoy
def NP_2_DF(default: DataContainer) -> DataFrame:
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

    match default:
        case DataFrame() | ParametricDataFrame():
            return default

        case OrderedPair() | ParametricOrderedPair():
            df = pd.DataFrame(default.y)
            return DataFrame(df=df)

        case OrderedTriple() | ParametricOrderedTriple():
            df = pd.DataFrame(default.z)
            return DataFrame(df=df)

        case Matrix() | ParametricMatrix():
            np_array = np.asarray(default.m)
            df = pd.DataFrame(np_array)
            return DataFrame(df=df)
        case Grayscale() | ParametricGrayscale():
            np_array = np.asarray(default.img)
            df = pd.DataFrame(np_array)
            return DataFrame(df=df)

        case Image() | ParametricImage():
            red = default.r
            green = default.g
            blue = default.b

            if default.a == None:
                merge = np.stack((red, green, blue), axis=2)
                merge = merge.reshape(-1, merge.shape[-1])
                df = pd.DataFrame(merge)
                return DataFrame(df=df)
            else:
                alpha = default.a
                merge = np.stack((red, green, blue, alpha), axis=2)
                merge = merge.reshape(-1, merge.shape[-1])
                df = pd.DataFrame(merge)
                return DataFrame(df=df)
        case _:
            raise ValueError(f"unsupported DataContainer type passed for NP_2_DF")
