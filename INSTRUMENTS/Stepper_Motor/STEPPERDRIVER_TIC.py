from flojoy import flojoy, DataContainer
from ticlib import TicUSB
from time import sleep


@flojoy
def STEPPERDRIVER_TIC(dc, params):
    tic = (
        TicUSB()
    )  # Declaration of the stepper driver (You can add serial number to specify the driver)

    tic.halt_and_set_position(0)  # Set the position to 0
    tic.set_current_limit(
        30
    )  # Set the current limit to the max the driver needs this current to work correctly
    tic.energize()  # Turn on the driver
    tic.exit_safe_start()  # The driver is now ready to receive commands
    positions = [
        int(params["position1"]),
        int(params["position2"]),
        int(params["position3"]),
        int(params["position4"]),
    ]  # Retrieving data from the CRTL parameters define by the User

    tic.set_target_position(positions[0])  # Set target position for the first movement
    tic.set_max_speed(
        int(params["speed1"])
    )  # Set maximum speed for the motor during first movement.
    sleep(2)

    tic.set_target_position(positions[1])  # Set target position for the second movement
    sleep(2)

    tic.set_max_speed(
        int(params["speed2"])
    )  # Set maximum speed for the motor during movement.
    tic.set_target_position(positions[2])
    sleep(2)

    tic.set_target_position(positions[3])
    sleep(2)

    tic.deenergize()
    tic.enter_safe_start()

    return DataContainer(x={"a": positions, "b": positions}, y=positions)


@flojoy
def STEPPERDRIVER_TIC_MOCK(dc, params):
    return DataContainer(x={"a": a, "b": b}, y=b)
