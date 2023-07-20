This example shows how to use the node Phidget22 to measure pressures from Flexiforce sensors using a Phidget InterfaceKit
The appendix contains all information about hardware requirements and sensor connections (Images).

After connecting the pressure sensors, place the nodes on Flojoy:

- The ['PHIDGET22'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/PHIDGET/PHIDGET22/PHIDGET22.py) node communicates with the Phidget interface kit. It measures voltages from the sensors and converts them into pressures thanks to the two calibration parameters (The user has to calibrate his sensors). This node has another parameter, 'n_sensors,' the number of pressure sensors in your experiment.

- The ['BAR'](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/BAR/BAR.py) node shows all pressure measurements on the same figure.

- The ['END'](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/TERMINATORS/END/END.py) node terminates the process.

### Calibration:

Apply known pressures (at least 4) and measure sensor voltages with the Phidget control panel. Plot the voltage as a function of the forces applied. You can choose the unit of your choice.
Find the linear equation (y=ax+b) between the voltage measured and the pressure applied on the sensor.
A and B are the calibration parameters used to convert voltage to pressure.

To update the measurements with time, you can add the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node and the [`GOTO`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/GOTO/GOTO.py) node to create a loop. (See [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) documentation for loop settings).
