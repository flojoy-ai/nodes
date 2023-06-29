import pandas as pd
from flojoy import flojoy, DataContainer


@flojoy
def JSON_2_DF(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Node to convert JSON type data into dataframe type data.
    It takes one JSON type data and converts it to dataframe type data.

    Parameters
    ----------
    None

    Returns
    -------
    dataframe
        Converted JSON value from the input
    """
    dc_input = dc_inputs[0]
    if dc_input.type == "ordered_pair":

        np_data = dc_input.y

        df = pd.DataFrame.from_dict(np_data)

        return DataContainer(type="dataframe", m=df)
    else:
        raise ValueError(
            f"unsupported DataContainer type passed for JSON_2_DF : {dc_input.type}"
        )
