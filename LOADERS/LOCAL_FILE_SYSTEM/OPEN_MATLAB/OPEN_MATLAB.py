from flojoy import flojoy, DataContainer, JobResultBuilder
from typing import Union
import numpy as np
from scipy.io import loadmat
from os import path
import pandas as pd


@flojoy
def OPEN_MATLAB(
    dc_inputs: list[DataContainer], params: dict
) -> Union[DataContainer, dict]:
    """The OPEN_MATLAB node loads a local file of the .mat file format.
    Note that if multiple 'tabs' of data are used, the number of rows
    must match in order to stack the arrays.

    Parameters
    ----------
    file_path : str
        path to the file to be loaded.

    Returns:
    --------
    DataContainer:
        type 'dataframe', m
    """
    file_path: str = params["path"]

    if file_path == '':
        file_path = path.join(
            path.dirname(path.abspath(__file__)),
            "assets",
            "default.mat",
        )

    if file_path[-4:] != '.mat':
        raise ValueError(f"File type {file_path[-4:]} unsupported.")

    if not path.exists(file_path):
        raise ValueError("File path does not exist!")

    mat = loadmat(file_path)
    key = list(mat.keys())[3:]
    X = mat[key[0]]
    Y = mat[key[1]]

    df = pd.DataFrame(np.hstack((X, Y)))

    return DataContainer(type="dataframe", m=df)
