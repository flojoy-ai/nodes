from flojoy import flojoy, DataFrame
import pandas as pd
from typing import cast


@flojoy
def ACCURACY(true_data : DataFrame, predicted_data : DataFrame) -> DataFrame:
    """The ACCURACY node takes two dataframes with the true and predicted labels from a classification task,
    and indicates whether the prediction was correct or not. These dataframes should both be single columns.

    Parameters
    ----------
    None

    Returns
    -------
    dataframe
        The input predictions dataframe, with an extra boolean column "prediction_correct".

    """
    
    true_df = cast(pd.DataFrame, true_data.m)
    predicted_df = cast(pd.DataFrame, predicted_data.m)

    predicted_df["prediction_correct"] = true_df.iloc[:, 0] == predicted_df.iloc[:, 0]
    return DataFrame(m=predicted_df)
