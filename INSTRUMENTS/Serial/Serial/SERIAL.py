from flojoy import flojoy, DataContainer
from time import time, sleep
import serial
import numpy as np
from datetime import datetime
import plotly.express as px


@flojoy
def SERIAL(v, params):
    '''
    Node to take simple time dependent 1d data from an Ardunio, or a similar serial device.
    For example you can record temperature following this tutorial:

    https://learn.adafruit.com/thermistor/using-a-thermistor

    with Serial.println(steinhart) as the only line printing.

    It is important that the last line Arduino is returning is the data with a new line at the end (i.e. println()).

    The other lines must be returned with print() with print(",") between each line. 

    For example:

    print(reading0)
    print(",")
    println(reading1)
    '''
    print('parameters passed to SERIAL: ', params)
    COM_PORT = params.get('com_port', '/dev/ttyUSB0') # The COM port to use (e.g.: Linux/Mac: '/dev/ttyUSB0' or Windows: COM1).
    BAUD = int(params.get('BAUD_RATE', 9600))
    NUM = int(params.get('num_readings', 100)) # Number of points to record. Length of recording ~= NUM * RECORD_PERIOD seconds.
    RECORD_PERIOD = float(params.get('record_period', 1)) # Period of recordings in seconds (i.e. the time between two recordings).
    # NUM = 5  # Debug


    ser = serial.Serial(COM_PORT, timeout=1, baudrate=BAUD)
    readings = []
    times = []
    s = ser.readline().decode()  # The first reading is commonly empty.
    # print(s)

    for i in range(NUM):
        ts = datetime.now()
        s = ser.readline().decode()
        if s != '':  # Some readings may be empty.
            # print('\n', 'debug: ', s, type(s), '\n')
            reading = s[:-2].split(',')
            readings.append(reading)

            ts = datetime.now()
            # date = f'{ts.year}{ts.month:02d}{ts.day:02d}'
            seconds = float(ts.hour * 3600 + ts.minute * 60 + ts.second + ts.microsecond / 10**6)
            # print('Seconds: ', seconds, 'Reading: ', reading)

            times.append(seconds)

            if len(times) > 0:
                time1 = seconds - times[i]
            else:
                time1 = 0.1  # Estimate of execution time 

            if time1 < RECORD_PERIOD:
                # print(f'sleeping for {RECORD_PERIOD - time1} seconds.')
                sleep(RECORD_PERIOD - time1)

    # print('')
    # print(readings)
    # print('')

    times = np.array(times)
    times -= times[0]
    # times = times.tolist()
    readings = np.array(readings)
    readings = readings.astype('float64')
    # y = [times, readings]

    # print(type(times), type(readings))
    # print('')
    # print(readings[:, 0])
    # print('')

    fig = px.line(x=times, y=readings[:, 0])

    return DataContainer(type='plotly', fig=fig, x=times, y=readings)


@flojoy
def Serial_MOCK (dc,params):

    print('Running mock version of Serial')

    x = np.linspace(0, 100, 100)
    y = np.linspace(0, 100, 100)

    return DataContainer(x=x, y=y)
