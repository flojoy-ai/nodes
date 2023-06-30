from flojoy import flojoy, DataContainer, DefaultParams
import pandas as pd
from typing import cast

@flojoy
def ACCURACY(true_data: DataContainer, predicted: DataContainer, default_parmas: DefaultParams) -> DataContainer:
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
    if len(dc_inputs) != 2:
        raise ValueError('ACCURACY node requires both true data and predicted data')
    predicted_data = dc_inputs[1]
    if true_data.type != 'dataframe':
        raise ValueError(f'unsupported DataContainer type passed to ACCURACY node for true: {true_data.type}')
    if predicted_data.type != 'dataframe':
        raise ValueError(f'unsupported DataContainer type passed to ACCURACY node for predicted: {predicted_data.type}')
    true_df = cast(pd.DataFrame, true_data.m)
    predicted_df = cast(pd.DataFrame, predicted_data.m)
    predicted_df['prediction_correct'] = true_df.iloc[:, 0] == predicted_df.iloc[:, 0]
    return DataContainer(type='dataframe', m=predicted_df)