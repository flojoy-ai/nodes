This example shows Flojoy's ability to record and display temperature measurements with a LABJACK U3 device and update them in a Loop. The appendix contains all information about hardware requirements and sensor connections (Images).


After connecting the temperature sensors to your LABJACK U3 device, place the nodes on Flojoy:


- The ['LABJACKU3'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/LABJACK/LABJACKU3/LABJACKU3.py) Node communicates with the LABJACKU3 device to extract temperature measurement from the sensors. This node has only one parameter to fix: the number of sensors (6 in this example).


- The ['BAR'](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/BAR/BAR.py) node displays all temperature measurements on the same figure.


- The ['END'](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/TERMINATORS/END/END.py) node terminates the process.


We want to update the results with the latest measurements. To do that, we add the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node and the [`GOTO`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/GOTO/GOTO.py) node to create a loop around our ['LABJACKU3'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/LABJACK/LABJACKU3/LABJACKU3.py) and ['BAR'](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/BAR/BAR.py) nodes. (See LOOP documentation for more information).
