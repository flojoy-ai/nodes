import numpy as np
import serial
from flojoy import flojoy, DataContainer


@flojoy
def KEITHLEY2400(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    IV curve measurement with a Keithley 2400 source meter, send voltages and measure currents
    """

    # Start serial communication with the instrument
    ser: serial = serial.Serial()

    # Specific parameters
    ser.port = params["comport"]  # Specify serial port for com
    ser.baudrate = params["baudrate"]  # Specify Baudrate

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

    voltages = dc_inputs[0].y
    currents_neg: list[float] = []  # measured currents

    for voltage in voltages:
        ser.write(b":SOUR:VOLT %f\n" % voltage)  # Source Tension (V)
        ser.write(b":OUTP ON\n")  # Instrument output open
        ser.write(b":INIT\n")  # Start measuring
        ser.write(b":FETC?\n")  # Retrieve the measured values

        current_str: str = (
            ser.readline().decode("ascii").strip()
        )  # Save answers in a string
        voltage_current_values: str = current_str.split(",")  # Split the string
        currents_neg.append(-float(voltage_current_values[1]))

        ser.write(b":OUTP OFF\n")  # Close output from Instrument

    # Close Serial Communication
    ser.close()

    return DataContainer(x={"a": voltages, "b": currents_neg}, y=currents_neg)


@flojoy
def KEITHLEY2400_MOCK(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Mock Function for Keithley2400 node"""

    voltages = dc_inputs[0].y
    currents_neg = []  # measured currents

    for voltage in voltages:
        voltage_current_values = voltages * 0.15
        currents_neg.append(-float(voltage_current_values[1]))

    return DataContainer(x={"a": voltages, "b": currents_neg}, y=currents_neg)
