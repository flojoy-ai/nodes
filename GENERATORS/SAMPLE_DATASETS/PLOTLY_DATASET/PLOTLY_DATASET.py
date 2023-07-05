from flojoy import flojoy, DataFrame, DefaultParams
from plotly.express import data


@flojoy
def PLOTLY_DATASET(default_params: DefaultParams) -> DataFrame:
    dataset_key = default_params["dataset_key"]
    df = getattr(data, dataset_key)()

    return DataFrame(m=df)
