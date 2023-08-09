from flojoy import flojoy, DataFrame
from plotly.express import data
from typing import Literal


@flojoy
def PLOTLY_DATASET(
    dataset_key: Literal[
        "wind",
        "iris",
        "carshare",
        "tips",
        "election",
        "experiment",
        "gapminder",
        "medals_long",
        "medals_wide",
        "stocks",
    ] = "wind"
) -> DataFrame:
    """The PLOTLY_DATASET node retrieves a pandas DataFrame from Plotly built in dataset using the provided dataset_key parameter and returns it wrapped in a flojoy DataFrame class.

    Parameters:
    -----------
    dataset_key: str

    Returns:
        DataFrame: A DataContainer object containing the retrieved pandas DataFrame.
    """
    df = getattr(data, dataset_key)()

    return DataFrame(df=df)