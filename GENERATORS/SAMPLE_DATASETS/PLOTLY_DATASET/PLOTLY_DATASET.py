from typing import Literal
from flojoy import flojoy, DataContainer, DefaultParams
from plotly.express import data

@flojoy
def PLOTLY_DATASET(default: DataContainer, default_parmas: DefaultParams, dataset_key: Literal['wind', 'iris', 'carshare', 'tips', 'election', 'experiment', 'gapminder', 'medals_long', 'medals_wide', 'stocks']='wind') -> DataContainer:
    df = getattr(data, dataset_key)()
    return DataContainer(type='dataframe', m=df)