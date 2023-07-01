from flojoy import flojoy, DataContainer, DefaultParams
import torch
from transformers import BartTokenizer, BartForConditionalGeneration
import pandas as pd


@flojoy
def BART_LARGE_CNN(
    default: DataContainer, default_params: DefaultParams
) -> DataContainer:
    """The BART_LARGE_CNN node takes an input dataframe with multiple rows and a single "text" column,
    and produces a dataframe with a single "summary_text" column.  The "summary_text" column contains a summary
    of the text in the corresponding row of the input dataframe.

    Parameters
    ----------
    None

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
    assert (
        len(input_df.columns.tolist()) == 1
    ), "Can only take a single-column dataframe as input"
    model = BartForConditionalGeneration.from_pretrained(
        "facebook/bart-large-cnn", revision="3d22493"
    )
    tokenizer = BartTokenizer.from_pretrained(
        "facebook/bart-large-cnn", revision="3d22493"
    )

    def _chunk_text(text):
        inputs_no_trunc = tokenizer(
            text, max_length=None, return_tensors="pt", truncation=False
        )
        chunks = []
        for i in range(
            0, len(inputs_no_trunc["input_ids"][0]), tokenizer.model_max_length
        ):
            chunk = inputs_no_trunc["input_ids"][0][i : i + tokenizer.model_max_length]
            chunks.append(torch.unsqueeze(chunk, 0))
        return chunks

    def _summarize_text(text):
        chunks = _chunk_text(text)
        summary_ids = [
            model.generate(
                chunk,
                num_beams=4,
                max_length=tokenizer.model_max_length // 2,
                early_stopping=True,
            )
            for chunk in chunks
        ]
        summaries = [
            "\n".join(
                [
                    tokenizer.decode(
                        g, skip_special_tokens=True, clean_up_tokenization_spaces=False
                    )
                    for g in id
                ]
            )
            for id in summary_ids
        ]
        return "\n".join(summaries)

    column = input_df.columns[0]
    output_df = pd.DataFrame(
        input_df[column].apply(_summarize_text).rename("summary_text")
    )
    return DataContainer(type="dataframe", m=output_df)
