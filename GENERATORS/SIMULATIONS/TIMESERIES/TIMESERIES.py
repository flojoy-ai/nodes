import numpy as np
from flojoy import flojoy, DataContainer
import pandas as pd
import traceback


@flojoy
def TIMESERIES(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Generates a random timeseries vector
    """

    try:
        np.random.seed(1)
        testing.N, testing.K = 1000, 1  # rows, columns
        df = pd.util.testing.makeTimeDataFrame(freq="MS")
        return DataContainer(x=df.index.to_numpy(), y=df["A"].to_numpy())
    except Exception:
        print(traceback.format_exc())
