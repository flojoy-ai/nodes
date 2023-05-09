from flojoy import flojoy, DataContainer
from ticlib import TicUSB
from time import sleep


@flojoy
def STEPPERDRIVER_TIC_KNOB(dc, params):
    tic = (
        TicUSB()
    )  # Declaration of the stepper driver (You can add serial number to specify the driver)

    tic.set_current_limit(
        30
    )  # Set the current limit to the max, the driver needs this current to work correctly
    tic.energize()  # Turn on the driver
    tic.exit_safe_start()  # The driver is now ready to receive commands
    tic.set_max_speed(2000000)  # Set maximum speed for the motor during first movement.

    knob_position = 2 * int(
        params["knob_value"]
    )  # Retrieving data from the CRTL parameters define by the User
    tic.halt_and_set_position(0)  # Set the position to 0
    tic.set_target_position(0)
    sleep(1)

    tic.set_target_position(knob_position)  # Set target position for the first movement
    sleep(1)

    tic.deenergize()
    tic.enter_safe_start()

    return DataContainer(x={"a": knob_position, "b": knob_position}, y=knob_position)


@flojoy
def STEPPERDRIVER_TIC_KNOB_MOCK(dc, params):
    return DataContainer(x={"a": a, "b": b}, y=b)
