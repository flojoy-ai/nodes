import numpy as np
from flojoy import flojoy, DataContainer
import pandas.testing as testing
import traceback


@flojoy
def TIMESERIES(dc, params):
    """
    Generates a random timeseries vector
    """

    try:
        np.random.seed(1)
        testing.N, testing.K = 1000, 1  # rows, columns
        df = testing.makeTimeDataFrame(freq="MS")
    except Exception:
        print(traceback.format_exc())

    return DataContainer(x=df.index.to_numpy(), y=df["A"].to_numpy())
