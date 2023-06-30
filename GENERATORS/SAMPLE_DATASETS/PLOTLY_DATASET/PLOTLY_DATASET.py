from flojoy import flojoy, DataContainer
from plotly.express import data


@flojoy
def PLOTLY_DATASET(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    dataset_key = params["dataset_key"]
    df = getattr(data, dataset_key)()

    return DataContainer(type="dataframe", m=df)
