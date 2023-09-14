from flojoy import flojoy, OrderedPair, Vector, node_initialization, NodeInitContainer
import serial
from typing import Optional


@flojoy(deps={"pyserial": "3.5"})
def SET_I_MEAS_V(
    init_container: NodeInitContainer,
    default: Optional[OrderedPair] = None,
    current: float = 0.1,
) -> OrderedPair:
    """The SET_I_MEAS_V lets you control the Keithley 2400 source meter using Serial communication (Rs232-USB cable).
   Users will set a current and measure the voltage from the device under test.


    Parameters
    -----------
    comport : string
         defines the serial communication port for the Keithley2400 sourcemeter.
    baudrate : float
         specifies the baud rate for the serial communication between the Keithley2400 and the computer
    current : float
         Specifies the current sourced by the Keithley2400
    """

    ser = init_container.get()
    if ser is None:
        raise ValueError("Serial communication is not open")

    # Keithley 2400 Configuration
    ser.write(b"*RST\n")  # reinitialisation of the instrument
    ser.write(b":SOUR:FUNC:MODE CURR\n")  # Sourcing current
    ser.write(b':SENS:FUNC "VOLT"\n')  # Sensing tension
    ser.write(
        b":SENS:CURR:PROT 1.05\n"
    )  # Current protection set at 1.05A (Keithley 2400)

    voltage: list[float] = []  # measured currents

    ser.write(b":SOUR:CURR %f\n" % current)  # Source Current (A)
    ser.write(b":OUTP ON\n")  # Instrument output open
    ser.write(b":INIT\n")  # Start measuring
    ser.write(b":FETC?\n")  # Retrieve the measured values

    voltage_str: str = (
        ser.readline().decode("ascii").strip()
    )  # Save answers in a string
    voltage_current_values: str = voltage_str.split(",")  # Split the string
    voltage = float(voltage_current_values[0])

    ser.write(b":OUTP OFF\n")  # Close output from Instrument

    # Close Serial Communication
    ser.close()

    return OrderedPair(x=voltage, y=current)


@node_initialization(for_node=SET_I_MEAS_V)
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
