from flojoy import flojoy, DataContainer

# import psutil (We need to download the library to get info about sensor)
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

    temperatures = psutil.sensors_temperatures()

    cpu_key = ""
    for key in temperatures.keys():
        for temp in temperatures[key]:
            if temp.label == "CPU temp":
                cpu_key = key
                break

    temp1 = psutil.sensors_temperatures()["system76_acpi"][0].current
    temp2 = temperatures[cpu_key][0].current

    memory_info = psutil.virtual_memory()
    memory_free = memory_info.available
    memory_free_go = memory_free / (1024**3)

    Temp = [temp1, memory_free_go]
    x_plot = ["CPU Temp (°C)", "RAM Available (Go)"]

    return DataContainer(type="ordered_pair", x=x_plot, y=Temp)


@flojoy
def CPU_TEMP_RAM_MOCK(dc, params):
    """
    Mock Version of the RaspberryPi node, return mock values
    """

    cpu_temp = 35
    raspberry_memory = 0

    return DataContainer(type="ordered_pair", x=cpu_temp, y=raspberry_memory)
