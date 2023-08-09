from flojoy import flojoy, OrderedPair
from typing import Optional
import u3  # Import the library from LabJackPython in order to use our U3-LV device


@flojoy(deps={"labjackpython": "2.1.0"})
def LABJACKU3(
    default: Optional[OrderedPair] = None, sensor_number: int = 1
) -> OrderedPair:
    """
    The LABJACKU3 node allows you to record and returns temperature measurements with a LABJACK U3 device.

    Parameters
    ----------
    number : int
         Defines the number of temperature sensors connected to the LabJack U3 device.
    """

    voltages: list[float] = []
    temperatures: list[float] = []
    temperatures_celsius: list[float] = []
    sensor_num: list[int] = []

    # Create an instance of U3 class
    d = u3.U3()
    # Config the U3 for daq from temperature sensors
    d.configIO(FIOAnalog=255, EIOAnalog=0)

    for i in range(0, sensor_number):
        sensor_num.append(i + 1)
        # Loop on the LabJack pins
        voltage: float = d.getAIN(i)
        # Convert Voltage into temperature in Celsius :
        temperature: float = voltage * 100.0
        temperature_celsius: float = (temperature - 32) / 1.8
        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celsius.append(temperature_celsius)

    return OrderedPair(x=sensor_num, y=temperatures_celsius)
