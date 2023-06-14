from flojoy import flojoy, DataContainer
from time import sleep
import serial
import numpy as np
from datetime import datetime
import plotly.graph_objects as go


@flojoy
def SERIAL_TIMESERIES(dc_inputs, params):
    """
    Node to take simple time dependent 1d data from an Ardunio,
    or a similar serial device.
    For example, you can record temperature following this tutorial:

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

    Parameters :
    ------------
    num_readings: int
        Number of points to record.
    record_period: float
        Length between two recordings in seconds.
    baudrate: int
        Baud rate for the serial device.
    comport: string
        COM port of the serial device

    num_readings * record_period is roughly the run length in seconds.
    """

    COM_PORT = params["comport"]
    BAUD = params["baudrate"]
    NUM = params["num_readings"]
    RECORD_PERIOD = params["record_period"]

    ser = serial.Serial(COM_PORT, timeout=1, baudrate=BAUD)
    readings = []
    times = []
    # The first reading is commonly empty.
    s = ser.readline().decode()

    for i in range(NUM):
        ts = datetime.now()
        s = ser.readline().decode()
        # Some readings may be empty.
        if s != "":
            reading = s[:-2].split(",")
            if len(reading) == 1:
                reading = reading[0]
            readings.append(reading)

            ts = datetime.now()
            seconds = float(
                ts.hour * 3600 + ts.minute * 60 + ts.second + ts.microsecond / 10**6
            )

            times.append(seconds)

            if len(times) > 0:
                time1 = seconds - times[i]
            else:
                # Estimate execution time.
                time1 = 0.1

            if time1 < RECORD_PERIOD:
                sleep(RECORD_PERIOD - time1)

    times = np.array(times)
    try:
        times -= times[0]
    except IndexError:
        raise IndexError("No data detected from the Arduino")

    readings = np.array(readings)
    readings = readings.astype("float64")
    # If there are two or more columns return a Plotly figure.
    if readings.ndim == 2:
        data = go.Line(x=times, y=readings[:, 0], mode="markers")
        fig = go.Figure(data=data)
        return DataContainer(type="plotly", fig=fig, x=times, y=readings)
    else:
        return DataContainer(x=times, y=readings)


@flojoy
def SERIAL_TIMESERIES_MOCK(dc, params):
    x = np.linspace(0, 100, 100)
    y = np.linspace(0, 100, 100)
    return DataContainer(x=x, y=y)
