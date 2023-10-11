import serial
from flojoy import flojoy, SerialConnection, TextBlob, Scalar, DataContainer
from typing import cast, Optional


@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def SCPI_WRITE(
    connection: SerialConnection,
    default: Optional[DataContainer] = None,
    command: str = "*IDN?",
) -> Scalar | TextBlob:
    """The SCPI_WRITE node writes a SCPI command to a connected bench-top instrument and returns the result.

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
    Scalar|TextBlob
        The return value from the bench-top instrument as a Scalar or TextBlob.
    """

    # Start serial communication with the instrument
    ser = cast(serial.Serial, connection.get_handle())

    if ser is None:
        raise ValueError("Serial communication is not open")

    CMD = command + "\n\r"

    ser.write(CMD.encode())

    resp = ser.readline().decode()

    try:
        resp = float(resp.rstrip("\n"))
    except:
        return TextBlob(resp)

    return Scalar(resp)
