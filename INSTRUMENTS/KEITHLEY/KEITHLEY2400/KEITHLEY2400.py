from flojoy import flojoy, OrderedPair, Vector
import serial


@flojoy(deps={"pyserial": "3.5"})
def KEITHLEY2400(
    default: OrderedPair | Vector, comport: str = "/dev/ttyUSB0", baudrate: float = 9600
) -> OrderedPair:
    """
    IV curve measurement with a Keithley 2400 source meter, send voltages and measure currents.

    Parameters
    -----------
    comport: string
         Comport defines the serial communication port for the Keithley2400 source meter.

    baudrate: float
         baudrate Specifies baud rate for the serial communication between the Keithley2400 and the computer.
    """

    # Start serial communication with the instrument
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

    # Keithley 2400 Configuration
    ser.write(b"*RST\n")  # reinitialisation of the instrument
    ser.write(b":SOUR:FUNC:MODE VOLT\n")  # Sourcing tension
    ser.write(b':SENS:FUNC "CURR"\n')  # Measuring current
    ser.write(
        b":SENS:CURR:PROT 1.05\n"
    )  # Current protection set at 1.05A (Keithley 2400)

    voltages = default.y
    currents_neg: list[float] = []  # measured currents

    for voltage in voltages:
        ser.write(b":SOUR:VOLT %f\n" % voltage)  # Source Tension (V)
        ser.write(b":OUTP ON\n")  # Instrument output open
        ser.write(b":INIT\n")  # Start measuring
        ser.write(b":FETC?\n")  # Retrieve the measured values

        current_str: str = (
            ser.readline().decode("ascii").strip()
        )  # Save answers in a string
        voltage_current_values: str = current_str.split(
            ",")  # Split the string
        currents_neg.append(-float(voltage_current_values[1]))

        ser.write(b":OUTP OFF\n")  # Close output from Instrument

    # Close Serial Communication
    ser.close()

    return OrderedPair(x=voltages, y=currents_neg)
