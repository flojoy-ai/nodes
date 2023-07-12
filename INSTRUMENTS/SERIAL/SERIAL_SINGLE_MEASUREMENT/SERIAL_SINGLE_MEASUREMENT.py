from flojoy import flojoy, OrderedPair
from time import sleep
from typing import Optional
import serial
import numpy as np
from datetime import datetime
import plotly.graph_objects as go


@flojoy(deps={"pyserial": "3.5"})
def SERIAL_SINGLE_MEASUREMENT(
    default: Optional[OrderedPair] = None,
    comport: str = "/dev/ttyUSB0",
    baudrate: float = 9600,
) -> OrderedPair:
    """
    The SERIAL_SINGLE_MEASUREMENT Node takes a single reading of data from an Ardunio,
    or a similar serial device.

    For example you can record temperature following this tutorial:
    https://learn.adafruit.com/thermistor/using-a-thermistor

    Parameters :
    ------------
    baudrate: Float
        Baud rate for the serial communication.

    comport: String
        Defines the comunication port on which the Serial device is connected
    """
    COM_PORT = comport
    BAUD = int(baudrate)

    ser = serial.Serial(COM_PORT, timeout=1, baudrate=BAUD)
    s = ""
    while s == "":
        s = ser.readline().decode()

    reading = s[:-2].split(",")

    reading = np.array(reading)  # Create an array
    reading = reading.astype("float64")  # Convert the array to float
    x = np.arange(0, reading.size)  # Create a second array

    results = OrderedPair(x=x, y=reading)

    return results
