from flojoy import flojoy, DataContainer
import psutil
import pandas as pd
import json


@flojoy
def CPU_TEMP(dc, params):
    """
    The CPU_TEMP Node returns the temperatures 
    measured on the computer running Flojoy with the function : psutil.sensor_temperatures().

    Parameters :
    ------------
    None
    """
    temperatures = psutil.sensors_temperatures()
    temp_df = pd.DataFrame.from_dict(temperatures, orient='index')
    temp_df['keys'] = temp_df.index
    temp_df = temp_df[["keys"] + list(temp_df.columns[:-1])]

    return DataContainer(type="dataframe", m=temp_df)
