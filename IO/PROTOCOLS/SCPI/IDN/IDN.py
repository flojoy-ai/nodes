import serial
from flojoy import flojoy, SerialConnection, TextBlob
from typing import cast

@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def IDN(
    connection: SerialConnection
) -> TextBlob:
    """The IDN node queries a device's identity through the universal *IDN? SCPI command.

    Parameters
    ----------
    connection: Serial
        The open connection with the device receiving the *IDN? SCPI command.

    Returns
    -------
    TextBlob
    """
    
    # Start serial communication with the instrument
    ser = cast(serial.Serial, connection.get_handle())

    if ser is None:
        raise ValueError("Serial communication is not open")
    
    ser.write('*IDN?\n'.encode())

    return TextBlob(text_blob=ser.readline())