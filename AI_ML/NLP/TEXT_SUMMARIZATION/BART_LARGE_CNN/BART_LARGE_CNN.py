from flojoy import flojoy, DataContainer
from transformers import pipeline
import pandas as pd


@flojoy
def BART_LARGE_CNN(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The BART_LARGE_CNN node takes an input dataframe with multiple rows and a single "text" column,
    and produces a dataframe with a single "summary_text" column.  The "summary_text" column contains a summary
    of the text in the corresponding row of the input dataframe.

    Parameters
    ----------
    max_length: int
        The maximum length of the summary text.
    min_length: int
        The minimum length of the summary text.
    do_sample: bool
        Whether or not to use sampling to generate the summary text. If do_sample is False, greedy decoding is used.
        Otherwise, probabilistic sampling is used for the next token.
    Returns:
    --------
    DataContainer:
        type 'dataframe' containing the summary text in the "summary_text" column.

    """
    if len(dc_inputs) != 1 or dc_inputs[0].type != "dataframe":
        raise ValueError(
            f"Invalid input, expected exactly one DataContainer of type 'dataframe'"
        )
    input_df = dc_inputs[0].m

    assert len(input_df.columns.tolist()) == 1, "Can only take a single-column dataframe as input"
    
    column = input_df.columns.tolist()[0]
    
    min_length = params.get("min_length", 30)
    max_length = params.get("max_length", 130)
    do_sample = params.get("do_sample", False)

    input_text = input_df[column].tolist()
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", revision="3d22493")
    output_df = pd.DataFrame.from_records(
        summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    )
    return DataContainer(type="dataframe", m=output_df)
