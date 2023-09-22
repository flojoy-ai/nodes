from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional


@flojoy()
def LM34(
    default: OrderedPair,
    calibration1: float = 100.0,
    calibration2: float = 32.0,
    calibration3: float = 1.8,
) -> OrderedPair:
    """The LM34 node allows you to convert voltages measured with a thermocouple (LM34) connected to a LabJack U3 device into temperatures.

    Parameters
    ----------
    Calibration1, Calibration2, Calibration3 : float
        Calibration parameters to convert voltage into temperature in Celcius.
    """

    temperatures_celsius: list[float] = []
    voltages = default.y
    sensor_num = default.x
    sensors_number = len(default.x)

    # Convert Voltage into temperature in Celsius :
    for i in range(0, sensors_number):
        temperature: float = voltages[i] * calibration1
        temperature_celsius: float = (temperature - calibration2) / calibration3
        temperatures_celsius.append(temperature_celsius)

    return OrderedPair(sensor_num, temperatures_celsius)
