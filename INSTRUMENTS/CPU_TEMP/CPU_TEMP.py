from flojoy import flojoy, DataContainer
import psutil
import pandas as pd
import json


@flojoy
def CPU_TEMP(dc, params):
    """
    The RASPBERRY_PI Node displays informations about the Raspberry pi which is
    used to run Flojoy such as CPU temperature and memory available on the device

    Parameters :
    ------------
    None
    """
    temperatures = psutil.sensors_temperatures()

    print("Temp Dictionnary")
    print(temperatures)

    temp_json = json.dumps(temperatures, indent=8)

    print("After Conversion to Json")
    print(type(temp_json))
    print(temp_json)

    return DataContainer(type="ordered_pair", x=None, y=[temperatures])
