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
        # Set the random seed for reproducibility
        np.random.seed(42)

        # Generate random time series data
        start_date = pd.Timestamp("2023-01-01")
        end_date = pd.Timestamp("2023-07-20")
        num_days = (end_date - start_date).days + 1
        timestamps = pd.date_range(start=start_date, end=end_date, freq="D")
        data = np.random.randn(num_days)  # Random data points

        df = pd.DataFrame({"Timestamp": timestamps, "Data": data})

        return DataContainer(type="dataframe", m=df)
    except Exception as e:
        print(traceback.format_exc())
        raise e
