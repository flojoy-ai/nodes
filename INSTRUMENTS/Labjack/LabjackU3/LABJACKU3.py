from flojoy import flojoy, DataContainer
import u3  # Import the library from LabJackPython in order to use our U3-LV device


@flojoy
def LABJACKU3(dc, params):
    """Takes a number of sensors as parameters and return their temperature measurement"""

    voltages = []
    temperatures = []
    temperatures_celsius = []
    sensor_num = []
    sensor_number = int(params["sensor_numbers"])

    # Create an instance of U3 class
    d = u3.U3()
    # Config the U3 for daq from temperature sensors
    d.configIO(FIOAnalog=255, EIOAnalog=0)

    for i in range(0, sensor_number):
        # Loop on the LabJack pins
        voltage = d.getAIN(i)
        # Convert Voltage into temperature in Celsius :
        temperature = voltage * 100.0
        temperature_celsius = (temperature - 32) / 1.8

        sensor_num.append(i + 1)
        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celsius.append(temperature_celsius)

    return DataContainer(
        x={"a": sensor_num, "b": temperatures_celsius}, y=temperatures_celsius
    )


@flojoy
def LABJACKU3_MOCK(dc, params):
    """Mock function for Labjack node"""
    voltages = []  # Declaration of variable
    temperatures = []
    temperatures_celsius = []
    sensor_number = 6  # Mock Number of sensors

    for i in range(1, sensor_number):
        # Mock Value
        voltage = 0.6
        # Convert Voltage into temperature in Celsius
        temperature = voltage * 100.0
        temperature_celsius = (temperature - 32) / 1.8

        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celsius.append(temperature_celsius)

    return DataContainer(
        x={"a": temperatures, "b": temperatures_celsius}, y=temperatures_celsius
    )
