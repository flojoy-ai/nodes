import json, can
from can.interface import Bus
from flojoy import SerialDevice, flojoy
from flojoy.connection_manager import DeviceConnectionManager


@flojoy(deps={"python-can": "4.2.2"})
def OPEN_BUS(device: SerialDevice, baudrate: int = 9600) -> None:
    """The OPEN_BUS node opens a CAN bus connection through a slcan-compatible USB-to-CAN adapter.

    Parameters
    ----------
    device: Serial
        The connected serial device.

    Returns
    -------
    TextBlob
    """

    can.rc['interface'] = 'slcan'
    can.rc['channel'] = device.get_port()
    can.rc['bitrate'] = 500000

    bus = Bus()

    DeviceConnectionManager.register_connection(device, can)

    return None
