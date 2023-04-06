from itertools import count

import matplotlib.pyplot as plt
import numpy as np
from flojoy import flojoy, DataContainer

import u3

@flojoy
def LABJACKU3 (dc, params):  # params {nombre de sensor}

    d = u3.U3()  # Create an instance of U3 class d.configU3()  # First Configuration for the Object, Ports Input
    # by default (0), if we want output, add FIODirection=255 in argument.

    d.configIO(FIOAnalog=255, EIOAnalog=0)  # Config the communication with the LabJack sensor

    voltages = []
    temperature = []
    temperature_celcius = []

    for i in params["numbers"]:
        voltages[i] = d.getAIN(i-1)
        print(voltages)

        temperature[i] = (voltages[i] * 100.0)
        temperature_celcius[i] = (temperature[i] - 32) / 1.8
        print(temperature_celcius)

    return DataContainer(x={"Numbers of sensors": params["numbers"], "Temperature": temperature}, y=temperature)



# ani= FuncAnimation(plt.gcf(),animate,interval=1000)        #Plot les 6 sensors en fonction du temps
# ani = FuncAnimation(plt.gcf(), animate2, interval=2000)  # Plot la Heatmap en fonction du temps

# plt.show()
