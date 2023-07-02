from flojoy import flojoy, DataContainer
import pandas as pd


@flojoy
def READ_CSV(
    default: DataContainer,
    file_path: str = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv",
):
    """
    Read a CSV file from disk or a URL, then return a dataframe.

    Parameters
    ----------
    file_path : str
        File path to the CSV file or an URL of CSV file

    """
    df = pd.read_csv(file_path)
    return DataContainer(type="dataframe", m=df)
