The Flojoy app example shows how to use the SERIAL_SINGLE_MEASUREMENT node to extract some measurements
received from an Arduino microcontroller and how to visualize them with Flojoy:

- The ['SERIAL_SINGLE_MEASUREMENT'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/SERIAL/SERIAL_SINGLE_MEASUREMENT/SERIAL_SINGLE_MEASUREMENT.py.py) node receives data from Serial communication with the Arduino and store the measured values in a table called reading. The Arduino prints new values on the serial console for each loop. The ['SERIAL_SINGLE_MEASUREMENT'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/SERIAL/SERIAL_SINGLE_MEASUREMENT/SERIAL_SINGLE_MEASUREMENT.py) node extracts a single measurement (It can contain multiple values, see output).


- The ['BAR'](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/BAR/BAR.py) node displays all values stored in the single measurement.

- The ['END'](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/TERMINATORS/END/END.py) node terminates the process.

(This example works with this Arduino code: arduino_example.ino):
The last line Arduino must return is the
data with a new line at the end (i.e. println()).

For example:

print(reading0)
print(",")
println(reading1)

The ['SERIAL_SINGLE_MEASUREMENT'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/SERIAL/SERIAL_SINGLE_MEASUREMENT/SERIAL_SINGLE_MEASUREMENT.py) node receives data from the Arduino serial console as a string and split it using "," as separators. Then it returns the values measured in a list called reading.

### Update Single Measurement with Loop:
To update the values received from the Arduino, use the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) and the [`GOTO`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/GOTO/GOTO.py) node to create a loop around the ['SERIAL_SINGLE_MEASUREMENT'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/SERIAL/SERIAL_SINGLE_MEASUREMENT/SERIAL_SINGLE_MEASUREMENT.py) and the ['BAR'](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/BAR/BAR.py). See app2.jpeg for an example.


The loop allows the user to update measurements, but only the last measurement will be saved and displayed.
To record all the measurements for a given period, use the ['SERIAL_TIMESERIES](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/SERIAL/SERIAL_TIMESERIES/SERIAL_TIMESERIES.py).