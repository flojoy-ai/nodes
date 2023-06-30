from flojoy import flojoy, DataContainer, DefaultParams
import pandas as pd
from typing import cast

@flojoy
def ONE_HOT_ENCODING(default: DataContainer, default_parmas: DefaultParams, categories: list[str | float | int]=[], columns: list[str | float | int]=[]) -> DataContainer:
    """The ONE_HOT_ENCODING node creates a one hot encoding from a dataframe containing categorical features.

    Parameters
    ----------
    categories : list of str or list of int, optional
        A list of categories, can be used to generate a one hot encoding without having to pass a dataframe.
    columns: list of str, optional
        Specifies the columns to encode. By default, the node will encode all categorical columns.

    Returns
    -------
    matrix
        The one hot encoding of the input features.
    """
    dc = dc_inputs[0] if len(dc_inputs) > 0 else None
    if dc is not None and dc.type != 'dataframe':
        raise ValueError(f"unsupported DataContainer type passed to ONE_HOT_ENCODING node: '{dc.type}'")
    if categories:
        data = pd.DataFrame({'category': categories})
        data['category'] = data['category'].astype('category')
        encoded = pd.get_dummies(data, dtype=int)
        return DataContainer(type='dataframe', m=encoded)
    if not dc:
        raise ValueError(f'ONE_HOT_ENCODING node did not receive input DataContainer')
    if columns:
        encoded = pd.get_dummies(dc.m[columns])
    else:
        df = cast(pd.DataFrame, dc.m)
        cat_df = df.select_dtypes(include=['object', 'category'])
        encoded = pd.get_dummies(cat_df, dtype=int)
    return DataContainer(type='dataframe', m=encoded)