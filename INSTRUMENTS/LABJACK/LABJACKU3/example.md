- This is a tutorial for using the node called LabJAck u3 in order to measure temperature with  temperature sensors (Add models)


**- Hardware required** : 
- A LabJack U3 LV daq 
- N temperature sensors (This tutorial will present connections with LM34Caz/Nopb : https://www.digikey.com/en/products/detail/texas-instruments/LM34CAZ-NOPB/117873)
- Connections cables (USB, Electronic cables)


**- Software required :**
- Flojoy software running (Go to the page -- Getting started/Installation)
- Exodriver for the LabJackU3 device and their requirements follow the guideline from : (https://labjack.com/pages/support?doc=/software-driver/installer-downloads/exodriver/)

**Connection :** 
You need to connect the LABJACKU3 Device to your computer with an USB cable. 

The you need to connect the temperature sensor to the Labjacku3 device. 
Before that if you use the LM34Caz/Nopb you'll need to add a small resistor between the Vout and the LabJack device to the circuit to protect the sensor (see pictures) :

![image](./assets/LABJACKU3_sensor.jpg)
*Connection on the LM34 temperature sensor* 

![image](./assets/LABJACKU3_connections.jpg)
*Connection between the sensor and the LabjackU3 device*

The connections are describe here on the pictures below (Left LabJack and right Sensors pin) : 
VS --> +Vs pin (Power supply from the computer transferred to the sensor with this connection)
Ground --> Ground Pin 
Ground --> Resistor Pin (See photos)
FI0 (For your first sensor) --> Vout pin on the sensor (Voltage are received with these FIi port where i goes from 0 to 7)

When you have these 4 connections, your setup is ready, you can place your sensor where you want to measure temperature and then start Flojoy.

**Node Management :** 

The LabJack Node doesn't need any data input, so it can be placed on the left on the interface : 

![image](./assets/LABJACKU3_nodes.png)
*Classical node placement for temperature measurements*

You'll need to set up one parameter in the CRTL panel which is the number of temperature sensors you are using for your experiment : 

After that you can choose your Visualisation node that fits your project to display the temperature measurements as you want.  

Also you can use the loop node (See documentation) in order to update the temperature measurements, you can set the parameters you want for the loops (Delay, number of loops, etc..) 

![image](./assets/LABJACKU3_nodeswithloop.png)
