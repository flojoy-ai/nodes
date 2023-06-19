from flojoy import flojoy, DataContainer
# import psutil (We need to download the library to get info about sensor)
import psutil


@flojoy
def RASPBERRY_PI(dc, params):
    """
    The RASPBERRYPI Node displays informations about the Raspberry pi which is 
    used to run Flojoy such as CPU temperature and memory available on the device

    Parameters : (Example from Serial for style)
    ------------
    baudrate: Float
        Baud rate for the serial communication.

    comport: String
        Define the COM port on which the Serial device is connected
    """

    # The idea is to detect if its raspberry

    cpu_temp = 35
    raspberry_memory = 0

    temperatures = psutil.sensors_temperatures()
    print("information")
    print(psutil.sensors_temperatures())

    cpu_key = ''
    for key, temps in temperatures.keys():
        for temp in temps:
            if temp.label == 'CPU temp':
                cpu_key = key
                break

    temp1 = psutil.sensors_temperatures()["system76_acpi"][0].current
    temp2 = temperatures[cpu_key][0].current

    Temp = [temp1, temp2]

    return DataContainer(type="ordered_pair", x=cpu_key, y=Temp)


print("temp du CPU")
print(temperature)


@flojoy
def RASPBERRY_PI_MOCK(dc, params):
    """
    Mock Version of the RaspberryPi node, return mock values 
    """

    cpu_temp = 35
    raspberry_memory = 0

    return DataContainer(type="ordered_pair", x=cpu_temp, y=raspberry_memory)
