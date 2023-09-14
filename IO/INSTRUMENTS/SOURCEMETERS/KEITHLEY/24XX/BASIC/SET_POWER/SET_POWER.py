from flojoy import flojoy, OrderedPair, node_initialization, NodeInitContainer, Literal
import serial
from typing import Optional


@flojoy(deps={"pyserial": "3.5"})
def SET_POWER(
    init_container: NodeInitContainer, mode: Literal["tension", "intensity"],
    default: Optional[OrderedPair] = None,
    current: float = 0.1,
    voltage: float = 2,
) -> OrderedPair:
    """The SET_POWER allows you to control the Keithley 2400 source meter. Set a current, and measure the voltage coming from the device under test. 

    Parameters
    -----------
    comport : string
         defines the serial communication port for the Keithley2400 sourcemeter.
    baudrate : float
         specifies the baud rate for the serial communication between the Keithley2400 and the computer
    current : int 
         Specifies the voltage sourced by the Keithley2400
    """

    ser = init_container.get()
    if ser is None:
        raise ValueError("Serial communication is not open")

    # Keithley 2400 Configuration
    ser.write(b"*RST\n")  # reinitialisation of the instrument

    if mode == "intensity":
        ser.write(b":SOUR:FUNC:MODE CURR\n")  # Sourcing Current
        ser.write(b':SENS:FUNC "VOLT"\n')  # Sensing Tension
        ser.write(
            b":SENS:CURR:PROT 1.05\n"
        )  # Current protection set at 1.05A (Keithley 2400)
        output = current
    else:
        ser.write(b":SOUR:FUNC:MODE VOLT\n")  # Sourcing tension
        ser.write(b':SENS:FUNC "CURR"\n')  # Sensing current
        ser.write(
            b":SENS:CURR:PROT 1.05\n"
        )  # Current protection set at 1.05A (Keithley 2400)

        output = voltage

    ser.write(b":OUTP OFF\n")  # Close output from Instrument

    # Close Serial Communication
    ser.close()

    return OrderedPair(x=mode, y=output)


@node_initialization(for_node=SET_POWER)
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
