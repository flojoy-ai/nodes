import numpy as np
from flojoy import flojoy, DataContainer, DefaultParams
import pandas as pd
import traceback

@flojoy
def TIMESERIES(default: DataContainer, default_parmas: DefaultParams) -> DataContainer:
    """
    Generates a random timeseries vector
    """
    try:
        np.random.seed(42)
        start_date = pd.Timestamp('2023-01-01')
        end_date = pd.Timestamp('2023-07-20')
        num_days = (end_date - start_date).days + 1
        timestamps = pd.date_range(start=start_date, end=end_date, freq='D')
        data = np.random.randn(num_days)
        df = pd.DataFrame({'Timestamp': timestamps, 'Data': data})
        return DataContainer(type='dataframe', m=df)
    except Exception as e:
        print(traceback.format_exc())
        raise e