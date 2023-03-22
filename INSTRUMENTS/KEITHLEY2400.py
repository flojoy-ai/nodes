import numpy as np
import serial
from flojoy import flojoy, DataContainer


@flojoy
def KEITHLEY2400 (dc,params):                  #params {comport, baudrate,timeout}

    # Serial communication with the instrument configuration
    ser = serial.Serial()

    #Specific parameters

    ser.port = params['comport'] # Secify serial port for com
    ser.baudrate = params['baudrate']  # Specify Baudrate
    ser.timeout = params['timeout']  # Specify delay for answer

    #General parameters
    ser.bytesize = serial.EIGHTBITS  # Specify Bites number
    ser.parity = serial.PARITY_NONE  # Specify Parity
    ser.stopbits = serial.STOPBITS_ONE  # Specify Stop bites


    # Keithley 2400 Configuration
    ser.write(b'*RST\n')  # reinitialisation of the instrument
    ser.write(b':SOUR:FUNC:MODE VOLT\n')  # Sourcing tension
    ser.write(b':SENS:FUNC "CURR"\n')  # Measuring current
    ser.write(b':SENS:CURR:PROT 1.05\n')  # Current protection set at 1.05A : Maximum for keithely 2400

    voltages = dc

    currents_neg = []  # measured currents

    for voltage in voltages:
        ser.write(b':SOUR:VOLT %f\n' % voltage)  # Source Tension (V)
        ser.write(b':OUTP ON\n')  # Instrument output open
        ser.write(b':INIT\n')  # Start measuring
        ser.write(b':FETC?\n')  # Retrieve the measured values

        current_str = ser.readline().decode('ascii').strip()  # Save answers in a string
        voltage_current_values = current_str.split(',')  # Split the string into measured values (Voltage, Current, Etc)
        currents_neg.append(-float(voltage_current_values[1]))  # Converts measured currents into float
        ser.write(b':OUTP OFF\n')  # Close output from Instrument

    # Close Serial Communication
    ser.close()

    return DataContainer(type="ordered pair", x={"Voltages": voltages},y={"Currents": currents_neg})
