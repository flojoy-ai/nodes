from flojoy import flojoy, DataContainer
import psutil


@flojoy
def CPU_RAM(dc, params):
    """
    The CPU_RAM node displays the available free memory of the computer running Flojoy.

    Parameters :
    ------------
    None
    """
    memory_info = psutil.virtual_memory()
    memory_free = memory_info.available
    memory_free_go = memory_free / (1024**3)

    return DataContainer(type='scalar', c=memory_free_go)
