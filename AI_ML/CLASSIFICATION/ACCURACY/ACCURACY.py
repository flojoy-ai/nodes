from flojoy import flojoy, Dataframe


@flojoy
def ACCURACY(
    true_data: Dataframe,
    predicted: Dataframe,
) -> Dataframe:
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
    true_df = true_data.m
    predicted_df = predicted.m
    predicted_df["prediction_correct"] = true_df.iloc[:, 0] == predicted_df.iloc[:, 0]
    return Dataframe(df=predicted_df)
