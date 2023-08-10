from os import path
from flojoy import flojoy, DataFrame
import pandas as pd


@flojoy(deps={"pyarrow": "12.0.1", "fastparquet": "2023.7.0"})
def OPEN_PARQUET(file_path: str = "") -> DataFrame:
    """
    The OPEN_PARQUET node loads a local file of the .parquet file format. It then returns the file as a pandas.Dataframe type.

    Parameters
    ----------
    file_path : str
        path to the file to be loaded

    Returns
    -------
    Dataframe
    """

    if file_path[-8:] != ".parquet":
        raise ValueError(f"File type {file_path[-8:]} unsupported.")

    if not path.exists(file_path):
        raise ValueError("File path does not exist!")

    read_parquet = pd.read_parquet(file_path)

    return DataFrame(df=read_parquet)
