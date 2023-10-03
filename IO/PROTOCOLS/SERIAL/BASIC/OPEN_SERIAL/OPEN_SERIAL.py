import json
import serial
from flojoy import SerialDevice, flojoy, TextBlob
from flojoy.connection_manager import DeviceConnectionManager


@flojoy(deps={"pyserial": "3.5"})
def OPEN_SERIAL(device: SerialDevice, baudrate: int = 9600) -> TextBlob:
    """The OPEN_SERIAL node opens a serial connection through your computer's USB or RS-232 port.

    Parameters
    ----------
    device: Serial
        The connected serial device.

    Returns
    -------
    TextBlob
    """

    ser = serial.Serial(
        port=device.get_port(),
        baudrate=baudrate,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1,
    )

    DeviceConnectionManager.register_connection(device, ser)

    return TextBlob(text_blob=json.dumps(ser.get_settings()))
