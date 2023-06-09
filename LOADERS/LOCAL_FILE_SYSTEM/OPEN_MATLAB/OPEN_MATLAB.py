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
    Note that only ordered pair (x, y) data can be loaded.

    If the x and y variables are inverted from the expected result,
    the xy_inverse parameter can be used as a correction.

    Parameters
    ----------
    xy_inverse : str
        inverse x and y outputs (x=y, y=x). True or False
    file_path : str
        path to the file to be loaded.

    Returns:
    --------
    DataContainer:
        type 'ordered_pair' x, y
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
