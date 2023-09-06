from flojoy import flojoy, Scalar, DataContainer
from typing import Optional
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument_drivers.tektronix.Keithley_2400 import Keithley2400

@flojoy(deps={"qcodes": "3.5"})
def KEITHLEY2400(default: Optional[DataContainer] = None, Voltage_range :int =10) -> OrderedPair:

# Create an instance of the Keithley2400 instrument
keithley = Keithley2400("keithley", "ASRL/dev/ttyUSB0::INSTR")

# Connect to the instrument
keithley.connect()

# Now you can use the instrument to perform measurements and control the power supply
# For example, you can set the voltage range
keithley.rangev(10)  # Set the voltage range to 10V

# You can also set the current range
keithley.rangei(1)  # Set the current range to 1A

# Set the voltage compliance
keithley.compliancev(5)  # Set the voltage compliance to 5V

# Set the current compliance
keithley.compliancei(0.1)  # Set the current compliance to 0.1A

# Set the output mode to voltage
keithley.mode("VOLT")  # Set the mode to voltage

# Set the sense mode to voltage
keithley.sense("VOLT")  # Set the sense mode to voltage

# Enable the output
keithley.output("on")  # Turn on the output

# Set the voltage level
keithley.volt(2)  # Set the voltage level to 2V

# Read the current
current = keithley.curr()  # Read the current

# Read the resistance
resistance = keithley.resistance()  # Read the resistance

# Disable the output
keithley.output("off")  # Turn off the output

# Disconnect from the instrument
keithley.disconnect()

x= [5]
y= [4] 


return OrderedPair(x,y)