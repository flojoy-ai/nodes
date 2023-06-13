The flojoy app example is showing how to use the SERIAL_SINGLE_MEASUREMENT node to extract some measurements 
received from an Arduino microcontroller and how to visualize them with Flojoy. 

Single measurement means that the measurements are all recorded at a given time when the nodes is called.
It receives data from Serial communication with the Arduino and store the measured values in a table called reading.
(The Arduino is printing new values on the serial console in each loop, with this node we reading value from one loop only).
 

An arduino can record measurements from different sensors and send them all to Flojoy (Single measurement does not mean single value)

In this example we show how the node works if 3 differents values are transmit from the arduino to Flojoy at a given time 
(These values have to be printed on the same line to be used properly by the node, check the arduino code : arduino_example.ino)

We choose the visualization node "BAR" to plot these 3 Mock values on the Flojoy app. 
It allows the user to see the 3 values at the same place. 


Update Single Measurement with Loop : 
Thanks to the flojoy software it is still possible to update the values received from the arduino by using the "LOOP" and the "GO TO" nodes.

The app2.txt show an example app where the values received form the Arduino are updated during each loop the plot will evolve for each Loop. 

This allow the user to update the measurements but at the end it'll save and display only the last measurement. 
If you want to record all the measurements for a given period you'll need to use the node "SERIAL_TIMESERIES".
