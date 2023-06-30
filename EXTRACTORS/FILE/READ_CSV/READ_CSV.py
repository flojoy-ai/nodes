from flojoy import flojoy, DataContainer
import pandas as pd


@flojoy
def READ_CSV(dc_inputs: list[DataContainer], params: dict[str, str]):
    """
    Read a CSV file from disk or a URL, then return a dataframe.

    Parameters
    ----------
    file_path : str
        File path to the CSV file or an URL of CSV file

    """
    file_path = params["file_path"]
    df = pd.read_csv(file_path)  # type: ignore
    return DataContainer(type="dataframe", m=df)
