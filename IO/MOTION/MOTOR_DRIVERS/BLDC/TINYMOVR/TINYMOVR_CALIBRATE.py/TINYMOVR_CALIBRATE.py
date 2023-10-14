from flojoy import flojoy, TextBlob

import can, json
from tinymovr.tee import init_tee
from tinymovr.config import get_bus_config, create_device

@flojoy(deps={"tinymovr": "1.6.2"})
def TINYMOVR_SERVO() -> TextBlob:
    """Discover and calibrate a connected tinymovr BLDC driver through a CANine USB-to-CAN controller.

    Parameters
    ----------
    None

    Returns
    -------
    TextBlob
        JSON representation of the CAN connection parameters.
    """

    bitrate = 1000000

    params = get_bus_config(["canine", "slcan_disco"])
    params["bitrate"] = bitrate
    init_tee(can.Bus(**params))
    tm = create_device(node_id=1)

    tm.controller.calibrate()

    return TextBlob(text_blob = json.dumps(params))