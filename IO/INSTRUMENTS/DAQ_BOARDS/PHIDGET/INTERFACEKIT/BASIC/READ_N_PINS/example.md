---
title: PHIDGET22
description: This example shows how to use the PHIDGET22 node to measure pressures from Flexiforce sensors using a Phidget Interface Kit.
keyword: [Python, Instrument, Phidget22 instrument control, Python integration with Phidget, Measurement and analysis, Python-based instrument control, Phidget22 integration techniques, Python-based measurement techniques, Enhance measurements with Python, Streamline Phidget usage, Accurate data analysis, Python control of Phidget22]
image: https://raw.githubusercontent.com/flojoy-ai/docs/main/docs/nodes/INSTRUMENTS/PHIDGET/PHIDGET22/examples/EX1/output.jpeg
--- 

This example shows how to use the `PHIDGET22` node to measure pressures from Flexiforce sensors using a Phidget Interface Kit. The appendix contains all information about hardware requirements and sensor connections (Images).

After connecting the pressure sensors, the following nodes are placed:

The [`PHIDGET22`](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/PHIDGET/PHIDGET22/PHIDGET22.py) node communicates with the Phidget Interface Kit. It measures voltages from the sensors and converts them into pressures because of the two calibration parameters (the user has to calibrate his sensors). This node has another parameter, `n_sensors`, the number of pressure sensors in your experiment.

The [`BAR`](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/BAR/BAR.py) node displays all pressure measurements on the same figure.

**Calibration:**

- Apply known pressures (at least 4) and measure sensor voltages with the Phidget control panel.
- Plot the voltage as a function of the forces applied. You can choose the unit of your choice.
- Find the linear equation (y=ax+b) between the voltage measured and the pressure applied on the sensor.
- A and B are the calibration parameters that convert voltage into pressure.

To update the measurements with time, you can add the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node to create a loop. (Refer to the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node documentation for the loop settings).