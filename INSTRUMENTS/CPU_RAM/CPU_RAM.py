from flojoy import flojoy, DataContainer
import psutil


@flojoy
def CPU_RAM(dc, params):
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

    description = "Memory available"

    return DataContainer(type="ordered_pair", x=description, y=memory_free_go)
