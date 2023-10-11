import serial, can
from flojoy import flojoy, SerialConnection, Vector, DataContainer, TextBlob
from typing import cast, Optional


@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def SEND_MESSAGE(
    connection: SerialConnection, 
    default: Vector | Optional[DataContainer] = None,
    arbitration_id: float = 0,
    is_extended_id: bool = True
) -> TextBlob:
    """The SEND_MESSAGE node writes an array of data (Vector) to the CAN bus.

    Inputs
    ------
    default: Vector
        The array of data to send to the CAN bus.

    Parameters
    ----------
    connection: Serial
        The open slcan connection - see the OPEN_BUS node.
    arbitration_id:
        Unique ID for message being sent.        
    is_extended_id: bool
        This flag controls the size of the arbitration_id field.      

    Returns
    -------
    TextBlob
        The message send attempt status.
    """

    # See the OPEN_BUS node
    bus = cast(serial.Serial, connection.get_handle())

    with can.Bus() as bus:
        msg = can.Message(
            arbitration_id = arbitration_id,
            data = default.v,
            is_extended_id = is_extended_id
        )
        try:
            bus.send(msg)
            resp = f"Message sent on {bus.channel_info}"
        except can.CanError:
            resp = "Message NOT sent"

    return TextBlob(resp)
