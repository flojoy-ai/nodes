import hid
import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def GAMEPAD(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    The GAMEPAD node reads the input from a gamepad and returns a DataContainer with the following structure:
    - it is of type ordered pair
    - the x value indicates how many buttons are available
    - the y value is a numpy array of booleans indicating which buttons are pressed
    """

    gamepad_device = None
    clicked_buttons = [False] * 12

    for device in hid.enumerate():
        if "gamepad" in device["product_string"].lower():
            gamepad_device = device

    if gamepad_device is None:
        print("ERROR: No gamepad found")
        return DataContainer(type="ordered_pair", x=0, y=np.array(clicked_buttons))

    gamepad = hid.device()
    gamepad.open(gamepad_device["vendor_id"], gamepad_device["product_id"])

    report = gamepad.read(64)

    """
    check backside buttons
    """
    if report[6] & 1:
        clicked_buttons[0] = True
    if report[6] & 2:
        clicked_buttons[1] = True

    """
    check rightside buttons
    """
    if report[5] & 0b01000000:
        clicked_buttons[2] = True

    if report[5] & 0b00100000:
        clicked_buttons[3] = True

    if report[5] & 0b10000000:
        clicked_buttons[4] = True

    if report[5] & 0b00010000:
        clicked_buttons[5] = True

    """
    check leftside buttons
    """
    if report[4] & 0b10000000:
        clicked_buttons[6] = True

    if report[4] == 0b00000000:
        clicked_buttons[7] = True

    if report[3] & 0b10000000:
        clicked_buttons[8] = True

    if report[3] == 0b00000000:
        clicked_buttons[9] = True

    """
    check center buttons
    """
    if report[6] & 0b00010000:
        clicked_buttons[10] = True

    if report[6] & 0b00100000:
        clicked_buttons[11] = True

    return DataContainer(type="ordered_pair", x=11, y=np.array(clicked_buttons))
