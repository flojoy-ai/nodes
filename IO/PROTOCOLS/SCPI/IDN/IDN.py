import serial
from flojoy import flojoy, SerialConnection, TextBlob
from typing import cast, Optional

@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def IDN(
    connection: SerialConnection, default: Optional[TextBlob] = None
) -> TextBlob:
    """The IDN node queries a device's identity through the universal *IDN? SCPI command.

    Inputs
    ------
    default: TextBlob
        A dummy TextBlob DataContainer - likely connected to the output of the OPEN_SERIAL node. This dummy input is intended to connect to the OPEN_SERIAL output to ensure that OPEN_SERIAL is executed first.    

    Parameters
    ----------
    connection: Serial
        The open connection with the device receiving the *IDN? SCPI command.

    Returns
    -------
    TextBlob
        The result of the *IDN? SCPI command.
    """
    
    # Start serial communication with the instrument
    ser = cast(serial.Serial, connection.get_handle())

    if ser is None:
        raise ValueError("Serial communication is not open")
    
    ser.write('*IDN?\n'.encode())

    return TextBlob(text_blob=ser.readline())