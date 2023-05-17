from flojoy import flojoy, DataContainer
from time import sleep
import serial
import numpy as np
from datetime import datetime
import plotly.graph_objects as go


@flojoy
def SERIAL(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Node to take simple time dependent 1d data from an Ardunio,
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
    num_readings: Number of points to record.
    record_period: Length between two recordings in seconds.
    BAUD_RATE: Baud rate for the serial device.
    com_port: COM port of the serial device

    num_readings * record_period is roughly the run length in seconds.
    """
    print("parameters passed to SERIAL: ", params)
    COM_PORT = params.get("com_port", "/dev/ttyUSB0")
    BAUD: int = int(params.get("BAUD_RATE", 9600))
    NUM: int = int(params.get("num_readings", 100))
    RECORD_PERIOD: float = float(params.get("record_period", 1))

    ser = serial.Serial(COM_PORT, timeout=1, baudrate=BAUD)
    readings: list[list[str]] = []
    times: list[float] = []
    # The first reading is commonly empty.
    s = ser.readline().decode()

    for i in range(NUM):
        ts = datetime.now()
        s = ser.readline().decode()
        # Some readings may be empty.
        if s != "":
            reading: list[str] = s[:-2].split(",")
            readings.append(reading)

            ts: datetime = datetime.now()
            seconds: float = float(
                ts.hour * 3600 + ts.minute * 60 + ts.second + ts.microsecond / 10**6
            )

            times.append(seconds)

            if len(times) > 0:
                time1: float = seconds - times[i]
            else:
                # Estimate execution time.
                time1: float = 0.1

            if time1 < RECORD_PERIOD:
                sleep(RECORD_PERIOD - time1)

    times: np.ndarray = np.array(times)
    times -= times[0]
    readings: np.ndarray = np.array(readings)
    readings = readings.astype("float64")
    # If there are two or more columns return a Plotly figure.
    if readings.ndim == 2:
        data = go.Line(x=times, y=readings[:, 0], mode="markers")
        fig = go.Figure(data=data)
        return DataContainer(type="plotly", fig=fig, x=times, y=readings)
    else:
        return DataContainer(x=times, y=readings)


@flojoy
def Serial_MOCK(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    print("Running mock version of Serial")

    x: np.ndarray = np.linspace(0, 100, 100)
    y: np.ndarray = np.linspace(0, 100, 100)

    return DataContainer(x=x, y=y)
