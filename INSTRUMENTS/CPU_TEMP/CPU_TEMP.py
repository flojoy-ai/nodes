from flojoy import flojoy, DataContainer
import psutil
import pandas as pd
import json


@flojoy
def CPU_TEMP_RAM(dc, params):
    """
    The RASPBERRY_PI Node displays informations about the Raspberry pi which is
    used to run Flojoy such as CPU temperature and memory available on the device

    Parameters :
    ------------
    None
    """
    memory_info = psutil.virtual_memory()
    memory_free = memory_info.available
    memory_free_go = memory_free / (1024**3)

    temperatures = psutil.sensors_temperatures()

    print("Temp Dictionnary")
    print(temperatures)

    temp_json = json.dumps(temperatures, indent=9)

    print("After Conversion to Json")
    print(temp_json)
    a = []
    b = 0

    # temp = pd.DataFrame.from_dict(temperatures, orient="index")
    # print(temp)

    table_temp = []
    # cpu_key = ""
    for item in temperatures.items():
        #    for temp in temperatures[key]:
        #        if temp.label == "CPU temp":
        #            cpu_key = key
        #            break
        b += 1
        table_temp.append(item)
        a.append(b)
        break

    print("Voici le tableau du dict decompose")
    print(table_temp)
    print(a)

    # temp = temperatures[cpu_key][0].current

    # cpu_data = [temp, memory_free_go]
    # data_description = ["CPU Temp (°C)", "RAM Available (Go)"]

    return DataContainer(type="ordered_pair", x=a, y=temp_json)
