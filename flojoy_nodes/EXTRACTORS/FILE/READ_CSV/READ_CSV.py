from flojoy import flojoy, DataFrame
import pandas as pd


@flojoy
def READ_CSV(
    file_path: str = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv",
) -> DataFrame:
    """The READ_CSV node reads a .csv file from disk or a URL, and then returns a dataframe.

    Parameters
    ----------
    file_path : str
        File path to the .csv file or an URL of a .csv file.

    Returns
    -------
    DataFrame
        DataFrame loaded from .csv file
    """

    df = pd.read_csv(file_path)  # type: ignore
    return DataFrame(df=df)
