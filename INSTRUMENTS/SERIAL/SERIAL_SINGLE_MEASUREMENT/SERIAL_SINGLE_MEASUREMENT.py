from flojoy import flojoy, DataContainer
from time import sleep
import serial
import numpy as np
from datetime import datetime
import plotly.graph_objects as go


@flojoy
def SERIAL_SINGLE_MEASUREMENT(dc_inputs, params):
    """
    The SERIAL_SINGLE_MEASUREMENT Node takes a single reading of data from an Ardunio,
    or a similar serial device.

    For example you can record temperature following this tutorial:

    https://learn.adafruit.com/thermistor/using-a-thermistor

    with Serial.println(steinhart) as the only line printing.

    It is important that the last line Arduino is returning is the
    data with a new line at the end (i.e. println()).

    The other lines must be returned with print()
    with print(",") between each line.

    For example:

    print(reading0)
    print(",")
    println(reading1)

    The SERIAL_SINGLE_MEASUREMENT receive data from the arduino serial console as a string and split
    it using "," as separators. Then it returns the values measured in a list names reading.


    Parameters :
    ------------
    baudrate: Float
        Baud rate for the serial communication.

    comport: String
        Define the COM port on which the Serial device is connected
    """
    COM_PORT = params["comport"]
    BAUD = int(params["baudrate"])

    ser = serial.Serial(COM_PORT, timeout=1, baudrate=BAUD)
    s = ""
    while s == "":
        s = ser.readline().decode()

    reading = s[:-2].split(",")

    reading = np.array(reading)  # Create an array
    reading = reading.astype("float64")  # Convert the array to float
    x = np.arange(0, reading.size)  # Create a second array

    return DataContainer(type="ordered_pair", x=x, y=reading)


@flojoy
def SERIAL_SINGLE_MEASUREMENT_MOCK(dc, params):
    print("Running mock version of Serial")

    x = np.linspace(0, 100, 100)
    y = np.linspace(0, 100, 100)

    return DataContainer(x=x, y=y)
