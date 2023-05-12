from flojoy import flojoy, DataContainer

import u3  # Import the library from LabJackPython in order to use our U3-LV device


@flojoy
def LABJACKU3(dc_inputs, params):  # params {nombre de sensor}
    d = u3.U3()  # Create an instance of U3 class d.configU3()
    d.configIO(
        FIOAnalog=255, EIOAnalog=0
    )  # Config the U3 for daq from temperature sensors

    voltages = []  # Declaration of variable
    temperatures = []
    temperatures_celcius = []
    N = int(params["numbers"])

    for i in range(1, N):  # Loop on the number of sensor you are using
        voltage = d.getAIN(i - 1)
        temperature = voltage * 100.0
        temperature_celcius = (
            temperature - 32
        ) / 1.8  # Convert Voltage into temperature in Celcius

        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celcius.append(temperature_celcius)  # Save measurements in lists
    return DataContainer(
        x={"a": temperatures, "b": temperatures_celcius}, y=temperatures_celcius
    )


@flojoy
def LABJACKU3_MOCK(dc_inputs, params):  # params {nombre de sensor}
    print("running mock version of LabJackU3, number of sensor is set to 6 by default")

    voltages = []  # Declaration of variable
    temperatures = []
    temperatures_celcius = []
    N = 6  # Mock Number of sensors

    for i in range(1, N):  # Loop on the number of sensor you are using
        voltage = 0.6  # Mock Value for the measured voltage
        temperature = voltage * 100.0
        temperature_celcius = (
            temperature - 32
        ) / 1.8  # Convert Voltage into temperature in Celcius
        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celcius.append(temperature_celcius)  # Save measurements in lists

    return DataContainer(
        x={"a": temperatures, "b": temperatures_celcius}, y=temperatures_celcius
    )
