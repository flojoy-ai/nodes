import serial
import traceback
from flojoy import flojoy, SerialConnection, TextBlob, Scalar
from typing import cast, Optional

@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def MEASURE_VOLTAGE(
    connection: SerialConnection, default: Optional[TextBlob]
) -> Scalar | TextBlob:
    """The MEASURE_VOLTAGE node queries an instrument's measured output voltage, such as a DMM or power supply.

    Inputs
    ------
    default: TextBlob
        An optional SCPI commmand string to override the MEASURE:VOLTAGE:DC? command.

    Parameters
    ----------
    connection: Serial
        The open serial connection with the instrument.

    Returns
    -------
    Scalar
    """
    
    # Start serial communication with the instrument
    ser = cast(serial.Serial, connection.get_handle())

    if ser is None:
        raise ValueError("Serial communication is not open")
    
    CMD = 'MEASURE:VOLTAGE:DC?\n\r'
    
    ser.write(CMD.encode())

    resp = ser.readline().decode()

    try:
        resp = float(resp.rstrip('\n'))
    except:
        print('Could not convert instrument response to a float', traceback.format_exc())
        return TextBlob(resp)
    
    return Scalar(resp)
