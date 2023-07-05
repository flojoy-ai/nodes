from flojoy import flojoy, OrderedPair
import LabJackPython
import u3  # Import the library from LabJackPython in order to use our U3-LV device


@flojoy
def LABJACKU3(numbers: int = 1) -> OrderedPair:
    """Takes a number of sensors as parameters and return their temperature measurement"""

    voltages: list[float] = []
    temperatures: list[float] = []
    temperatures_celsius: list[float] = []
    sensor_num: list[int] = []
    sensor_number: int = numbers

    # Create an instance of U3 class
    d = u3.U3()
    # Config the U3 for daq from temperature sensors
    d.configIO(FIOAnalog=255, EIOAnalog=0)

    for i in range(0, sensor_number):
        # Loop on the LabJack pins
        voltage: float = d.getAIN(i)
        # Convert Voltage into temperature in Celsius :
        temperature: float = voltage * 100.0
        temperature_celsius: float = (temperature - 32) / 1.8

        sensor_num.append(i + 1)
        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celsius.append(temperature_celsius)

    return OrderedPair(
        x={"a": sensor_num, "b": temperatures_celsius},
        y=temperatures_celsius,
    )


@flojoy
def LABJACKU3_MOCK() -> OrderedPair:
    """Mock function for Labjack node"""
    voltages: list[float] = []  # Declaration of variable
    temperatures: list[float] = []
    temperatures_celsius: list[float] = []
    sensor_number = 6  # Mock Number of sensors
    voltage = 0.6  # Mock value

    for i in range(1, sensor_number):
        # Convert Voltage into temperature in Celsius
        temperature: float = voltage * 100.0
        temperature_celsius: float = (temperature - 32) / 1.8

        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celsius.append(temperature_celsius)

    return OrderedPair(
        x={"a": temperatures, "b": temperatures_celsius}, y=temperatures_celsius
    )
