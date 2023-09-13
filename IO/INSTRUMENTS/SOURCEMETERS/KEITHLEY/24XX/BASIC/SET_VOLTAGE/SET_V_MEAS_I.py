from flojoy import flojoy, OrderedPair, Vector, node_initialization, NodeInitContainer
import serial
from typing import Optional


@flojoy(deps={"pyserial": "3.5"})
def SET_V_MEAS_I(
    init_container: NodeInitContainer, default: Optional[OrderedPair] = None,
    voltage: int = 1,
) -> OrderedPair:
    """The SET_V_MEAS_I allows you to control the Keithley 2400 source meter. Set a voltage, and measure the current coming from the device under test. 

    Parameters
    -----------
    comport : string
         defines the serial communication port for the Keithley2400 sourcemeter.
    baudrate : float
         specifies the baud rate for the serial communication between the Keithley2400 and the computer
    voltage : int 
         Specifies the voltage sourced by the Keithley2400
    """

    ser = init_container.get()
    if ser is None:
        raise ValueError("Serial communication is not open")

    # Keithley 2400 Configuration
    ser.write(b"*RST\n")  # reinitialisation of the instrument
    ser.write(b":SOUR:FUNC:MODE VOLT\n")  # Sourcing tension
    ser.write(b':SENS:FUNC "CURR"\n')  # Measuring current
    ser.write(
        b":SENS:CURR:PROT 1.05\n"
    )  # Current protection set at 1.05A (Keithley 2400)

    current: list[float] = []  # measured currents

    ser.write(b":SOUR:VOLT %f\n" % voltage)  # Source Tension (V)
    ser.write(b":OUTP ON\n")  # Instrument output open
    ser.write(b":INIT\n")  # Start measuring
    ser.write(b":FETC?\n")  # Retrieve the measured values

    current_str: str = (ser.readline().decode(
        "ascii").strip())  # Save answers in a string
    voltage_current_values: str = current_str.split(",")  # Split the string
    current = float(voltage_current_values[1])

    ser.write(b":OUTP OFF\n")  # Close output from Instrument

    # Close Serial Communication
    ser.close()

    return OrderedPair(x=voltage, y=current)


@node_initialization(for_node=SET_V_MEAS_I)
def init(comport: str = "/dev/ttyUSB0", baudrate: float = 9600):
    ser: serial = serial.Serial()

    # Specific parameters
    ser.port = comport  # Specify serial port for com
    ser.baudrate = baudrate  # Specify Baudrate

    # General parameters
    ser.bytesize = serial.EIGHTBITS  # Specify Bites number
    ser.parity = serial.PARITY_NONE  # Specify Parity
    ser.stopbits = serial.STOPBITS_ONE  # Specify Stop bites
    ser.timeout = 1
    # Open Serial Com
    ser.open()

    return ser
