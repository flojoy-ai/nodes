from flojoy import flojoy, DataContainer
import psutil


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

    cpu_key = ""
    for key in temperatures.keys():
        for temp in temperatures[key]:
            if temp.label == "CPU temp":
                cpu_key = key
                break

    temp = temperatures[cpu_key][0].current

    cpu_data = [temp, memory_free_go]
    data_description = ["CPU Temp (°C)", "RAM Available (Go)"]

    return DataContainer(type="ordered_pair", x=data_description, y=cpu_data)
