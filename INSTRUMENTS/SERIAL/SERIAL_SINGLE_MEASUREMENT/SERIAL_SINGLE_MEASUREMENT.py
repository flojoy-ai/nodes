from flojoy import flojoy, DataContainer
from time import sleep
import serial
import numpy as np
from datetime import datetime
import plotly.graph_objects as go


@flojoy
def SERIAL_SINGLE_MEASUREMENT(dc_inputs, params):
    """
    Node to take a single reading of data from an Ardunio,
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

    This node will receive the data from the arduino as a string and will split
    the string using "," as separators.
    It will return the measurement in a table of float that we'll be able to plot using visualization nodes from Flojoy


    params:
    BAUD_RATE: Baud rate for the serial device.
    com_port: COM port of the serial device
    """
    print("parameters passed to SERIAL_TIMESERIES: ", params)
    COM_PORT = params["comport"]
    BAUD = int(params["baudrate"])

    ser = serial.Serial(COM_PORT, timeout=1, baudrate=BAUD)
    # The first reading is commonly empty.
    s = ser.readline().decode()

    # Some readings may be empty at first because it takes time before receiving the data. Try a second time if so.
    if s != "":
        reading = s[:-2].split(",")
    else:
        s = ser.readline().decode()
        print(" decode testbis: ", str(s))
        reading = s[:-2].split(",")  # Store the measured values

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
