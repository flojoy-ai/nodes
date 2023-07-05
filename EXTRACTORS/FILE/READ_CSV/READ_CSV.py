from flojoy import flojoy, DataFrame, DefaultParams
import pandas as pd


@flojoy
def READ_CSV(default_params: DefaultParams):
    """
    Read a CSV file from disk or a URL, then return a dataframe.

    Parameters
    ----------
    file_path : str
        File path to the CSV file or an URL of CSV file

    """
    file_path = default_params["file_path"]
    df = pd.read_csv(file_path)  # type: ignore
    return DataFrame(m=df)