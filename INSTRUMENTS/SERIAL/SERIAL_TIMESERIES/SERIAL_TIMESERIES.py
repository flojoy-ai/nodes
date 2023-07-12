from flojoy import flojoy, OrderedPair
from time import sleep
from typing import Optional
import serial
import numpy as np
from datetime import datetime
import plotly.graph_objects as go


@flojoy(deps={"pyserial": "3.5"})
def SERIAL_TIMESERIES(
    default: Optional[OrderedPair] = None,
    comport: str = "/dev/ttyUSB0",
    baudrate: float = 9600,
    num_readings: int = 100,
    record_period: float = 1,
) -> OrderedPair:
    """
    The SERIAL_TIMESERIES Node extract simple time dependent 1d data from an Ardunio,
    or a similar serial device.

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

    COM_PORT = comport
    BAUD = baudrate
    NUM = num_readings
    RECORD_PERIOD = record_period

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

    results = OrderedPair(x=times, y=readings)

    return results
