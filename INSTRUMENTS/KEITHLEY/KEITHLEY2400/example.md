This example app shows how to record an Iv curve using Flojoy, a Keithley2400 source meter, and a computer :

You need four nodes to record an IV curve :

- The ['LINSPACE'](https://github.com/flojoy-io/nodes/blob/main/GENERATORS/SIMULATIONS/LINSPACE/LINSPACE.py) node defines the voltages range sent to the electronic device.The user defines the voltage range by setting these parameters with Numeric Input:

  - LINSPACE START: Define your first Voltage
  - LINSPACE END: Define your last Voltage
  - LINSPACE STEP: Define the number of voltages between the first and the last one.

- The ['KEITHLEY2400'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/KEITHLEY/KEITHLEY2400/KEITHLEY2400.py) node will communicate with the source meter by serial communication to send voltages and measure currents from the device. This node has two communication parameters set by the user after connecting the Keithley2400 to his computer:

  - KEITHLEY2400 COMPORT: Define your communication port where the source meter is connected (Default is: /dev/tty/USBO (Linux))
  - KEITHLEY2400 BAUDRATE: Define the Baud rate of your communication protocol (Default is: 9600, the value has to correspond to the Instrument settings)

- The ['LINE'](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/LINE/LINE.py) node will display the I-V curve by plotting the currents received from the device in function of the voltages transmitted to the device.

- The ['END'](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/TERMINATORS/END.py) node terminates the process.

When the setup is ready, and the parameters above are well defined, you can start the experiment (Turn on the source meter and click the 'PLAY' button).
