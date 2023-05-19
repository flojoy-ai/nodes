from flojoy import flojoy, DataContainer
from time import sleep
import serial
import numpy as np
from datetime import datetime
import plotly.graph_objects as go


@flojoy
def SERIAL_SINGLE_READING(dc_inputs, params):
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

    If there is more than one column, the SELECT_ARRAY node must be
    used after this node.

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

    # Some readings may be empty. Try a second time if so.
    if s != "":
        reading = s[:-2].split(",")
    else:
        s = ser.readline().decode()
        reading = s[:-2].split(",")

    reading = np.array(reading)
    reading = reading.astype("float64")

    data = go.Line(x=[0], y=[0], mode="markers")
    fig = go.Figure(data=data)
    return DataContainer(type="plotly", fig=fig, x=[0], y=reading)


@flojoy
def SERIAL_SINGLE_READING_MOCK(dc, params):
    print("Running mock version of Serial")

    x = np.linspace(0, 100, 100)
    y = np.linspace(0, 100, 100)

    return DataContainer(x=x, y=y)
