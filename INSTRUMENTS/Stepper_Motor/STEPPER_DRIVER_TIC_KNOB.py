from flojoy import flojoy, DataContainer

# Import the TicUSB library to send command to Tic drivers with USB connection
from ticlib import TicUSB
from time import sleep


@flojoy
def STEPPER_DRIVER_TIC_KNOB(
    dc_inputs: list[DataContainer], params: dict
) -> DataContainer:
    """
    Takes knob position as parameters to control the rotation of the motor and allow to control position
    and speed of a motor with a TIC driver
    """

    speed = int(params["speed"])
    sleep_time = int(params["sleep_time"])
    current_limit = int(params["sleep_time"])

    # Converting the knob value into a position
    knob_position = 2 * int(params["knob_value"])

    # Declaration of the stepper driver (You can add serial number to specify the driver)
    tic = TicUSB()
    tic.set_current_limit(current_limit)  # Set the current limit for the driver TIC
    tic.energize()  # Turn on the driver
    tic.exit_safe_start()  # The driver is now ready to receive commands
    tic.set_max_speed(speed)  # Set maximum speed for the motor during first movement.

    tic.halt_and_set_position(0)  # Set initial position to origin
    sleep(sleep_time)

    tic.set_target_position(knob_position)  # Set target position for the first movement
    sleep(sleep_time)

    tic.deenergize()
    tic.enter_safe_start()

    return DataContainer(x={"a": knob_position, "b": knob_position}, y=knob_position)


@flojoy
def STEPPER_DRIVER_TIC_KNOB_MOCK(
    dc_inputs: list[DataContainer], params: dict
) -> DataContainer:
    """Mock function for the stepper driver node"""
    positions = [50, 100, 150, 200]  # Setting default positions
    speeds = [50000, 1000000, 150000, 200000]  # Setting default speeds
    return DataContainer(x={"a": positions, "b": speeds}, y=positions)
