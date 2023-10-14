import serial, traceback
from flojoy import flojoy, SerialConnection, TextBlob, DataContainer
from typing import cast, Optional


@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def PROLOGIX_VER(
    connection: SerialConnection,
    default: Optional[DataContainer] = None,
) -> TextBlob:
    """The PROLOGIX_VER command queries the Prologix USB-to-GPIB firmware version.

    Inputs
    ------
    default: DataContainer
        Any DataContainer - likely connected to the output of the OPEN_SERIAL node.

    Parameters
    ----------
    connection: Serial
        The open serial connection with the instrument.

    Returns
    -------
    TextBlob
        The Prologix controller available commands.
    """

    try:
        # Start serial communication with the instrument
        ser = cast(serial.Serial, connection.get_handle())
        if ser is None:
            raise ValueError("Serial communication is not open")
        ser.write(b"++ver\r\n")
        s = ser.read(1000).decode()
    except:
        s = traceback.format_exc()

    return TextBlob(s)
