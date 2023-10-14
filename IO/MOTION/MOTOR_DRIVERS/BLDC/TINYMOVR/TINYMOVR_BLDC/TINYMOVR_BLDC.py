from flojoy import flojoy, DataContainer, Vector
import time
from typing import Optional

from tinymovr.tee import init_tee
from tinymovr.config import get_bus_config, create_device

@flojoy(deps={"tinymovr": "1.6.2"})
def TINYMOVR_BLDC(
    default: Vector | Optional[DataContainer] = None,
    sleep: float = 0,
    velocity: float = 80000
) -> None:
    """Direct a tinymovr BLDC driver through a vector of positions atfixed velocity.

    Input
    -----


    Parameters
    ----------
    sleep: float
        Time to wait between movements
    velocity: float
        Tinymovr servo velocity

    Returns
    -------
    None
    """

    # Connect to servo over CAN network
    # TODO: Consider saving Avlos tm Python object in Flojoy's hardware device context manager
    # Reference: https://github.com/tinymovr/avlos

    bitrate = 1000000

    params = get_bus_config(["canine", "slcan_disco"])
    params["bitrate"] = bitrate
    init_tee(can.Bus(**params))
    tm = create_device(node_id=1)

    # Set servo velocity

    tm.controller.velocity_mode()
    tm.controller.velocity.setpoint = velocity

    # Move servo through vector of positions

    positions = default
    for pos in positions:
        tm.controller.position.setpoint = pos
        time.sleep(sleep)

    return None