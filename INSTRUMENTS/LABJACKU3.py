from flojoy import flojoy, DataContainer

import u3                 #Import the library from LabJackPython in order to use our U3-LV device

@flojoy
def LABJACKU3(dc, params):                           # params {nombre de sensor}
    d = u3.U3()                                      # Create an instance of U3 class d.configU3()
    d.configIO(FIOAnalog=255, EIOAnalog=0)           # Config the U3 for daq from temperature sensors

    voltages = []                                    # Declaration of variable
    temperatures = []
    temperatures_celcius = []
    N = int(params["numbers"])

    for i in range(1, N):                            #Loop on the number of sensor you are using
        voltage = d.getAIN(i-1)
        temperature = voltage * 100.0
        temperature_celcius = (temperature - 32) / 1.8 # Convert Voltage into temperature in Celcius

        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celcius.append(temperature_celcius)  # Save measurements in lists
    return DataContainer(x={"Temperature": temperatures, "Temp en Celcius": temperatures_celcius}, y=temperatures_celcius)
