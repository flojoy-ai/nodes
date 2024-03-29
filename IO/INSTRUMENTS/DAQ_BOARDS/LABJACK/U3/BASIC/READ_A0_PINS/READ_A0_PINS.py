from flojoy import flojoy, OrderedPair, node_initialization, NodeInitContainer
from typing import Optional
import u3  # Import the library from LabJackPython in order to use our U3-LV device


@flojoy(deps={"labjackpython": "2.1.0"})
def READ_A0_PINS(
    init_container: NodeInitContainer,
    default: Optional[OrderedPair] = None,
    sensor_number: int = 1,
) -> OrderedPair:
    """The READ_A0_PINS node allows you to record and return voltages from a sensor connected to a LABJACK U3 device.

    The SENSOR node can be used to convert voltage into temperature measurements.

    Parameters
    ----------
    number : int
        Defines the number of temperature sensors connected to the LabJack U3 device.
    """

    voltages: list[float] = []

    sensor_num: list[int] = []

    d = init_container.get()
    if d is None:
        raise ValueError("LabJack U3 device not initialized")

    for i in range(0, sensor_number):
        sensor_num.append(i + 1)
        # Loop on the LabJack pins
        voltage: float = d.getAIN(i)
        voltages.append(voltage)

    return OrderedPair(x=sensor_num, y=voltages)


@node_initialization(for_node=READ_A0_PINS)
def init():
    d = u3.U3()
    d.configIO(FIOAnalog=255, EIOAnalog=0)

    return d
