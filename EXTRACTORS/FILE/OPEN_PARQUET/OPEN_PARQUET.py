from os import path
from flojoy import flojoy, DataFrame, DefaultParams
import pandas as pd


@flojoy
def OPEN_PARQUET(default_params: DefaultParams
) -> DataFrame:
    """
    The OPEN_PARQUET node loads a local file of the .parquet file format.
    It returns the file in pandas.Dataframe type.

    Parameters
    ----------
    file_path : str
        path to the file to be loaded.

    Returns:
    --------
    DataContainer:
        type 'dataframe', m
    """

    file_path = default_params["file_path"]

    if file_path[-8:] != ".parquet":
        raise ValueError(f"File type {file_path[-8:]} unsupported.")

    if not path.exists(file_path):
        raise ValueError("File path does not exist!")

    read_parquet = pd.read_parquet(file_path)

    return DataFrame(m=read_parquet)
