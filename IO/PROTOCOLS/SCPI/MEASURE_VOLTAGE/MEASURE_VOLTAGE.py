import serial
import traceback
from flojoy import flojoy, SerialConnection, TextBlob, Scalar, DataContainer
from typing import cast, Optional


@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def MEASURE_VOLTAGE(
    connection: SerialConnection, default: Optional[DataContainer] = None
) -> Scalar | TextBlob:
    """The MEASURE_VOLTAGE node queries an instrument's measured output voltage, such as a DMM or power supply.

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
        The measured voltage as a Scalar or an exception error as a TextBlob.
    """

    # Start serial communication with the instrument
    ser = cast(serial.Serial, connection.get_handle())

    if ser is None:
        raise ValueError("Serial communication is not open")

    CMD = "MEASURE:VOLTAGE:DC?\n\r"

    ser.write(CMD.encode())

    resp = ser.readline().decode()

    try:
        resp = float(resp.rstrip("\n"))
    except:
        print(
            "Could not convert instrument response to a float", traceback.format_exc()
        )
        return TextBlob(resp)

    return Scalar(resp)
