import serial
from flojoy import flojoy, DataContainer


@flojoy
def KEITHLEY2400(
    default: DataContainer,
    comport: str = "/dev/ttyUSB0",
    baudrate: float = 9600,
) -> DataContainer:
    """
    IV curve measurement with a Keithley 2400 source meter, send voltages and measure currents
    """
    ser: serial = serial.Serial()
    ser.port = params["comport"]
    ser.baudrate = params["baudrate"]
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 1
    ser.open()
    ser.write(b"*RST\n")
    ser.write(b":SOUR:FUNC:MODE VOLT\n")
    ser.write(b':SENS:FUNC "CURR"\n')
    ser.write(b":SENS:CURR:PROT 1.05\n")
    voltages = dc_inputs[0].y
    currents_neg: list[float] = []
    for voltage in voltages:
        ser.write(b":SOUR:VOLT %f\n" % voltage)
        ser.write(b":OUTP ON\n")
        ser.write(b":INIT\n")
        ser.write(b":FETC?\n")
        current_str: str = ser.readline().decode("ascii").strip()
        voltage_current_values: str = current_str.split(",")
        currents_neg.append(-float(voltage_current_values[1]))
        ser.write(b":OUTP OFF\n")
    ser.close()
    return DataContainer(x={"a": voltages, "b": currents_neg}, y=currents_neg)


@flojoy
def KEITHLEY2400_MOCK(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Mock Function for Keithley2400 node"""
    voltages = dc_inputs[0].y
    currents_neg = []
    for voltage in voltages:
        voltage_current_values = voltages * 0.15
        currents_neg.append(-float(voltage_current_values[1]))
    return DataContainer(x={"a": voltages, "b": currents_neg}, y=currents_neg)
