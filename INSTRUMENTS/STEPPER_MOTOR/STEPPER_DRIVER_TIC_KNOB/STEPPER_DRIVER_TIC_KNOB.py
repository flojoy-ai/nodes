from flojoy import flojoy, OrderedPair
# Import the TicUSB library to send command to Tic drivers with USB connection
from ticlib import TicUSB
from time import sleep


@flojoy(deps={"ticlib": "0.2.2"})
def STEPPER_DRIVER_TIC_KNOB(
        default: OrderedPair = None,
        knob_value: int = 0,
        current_limit: int = 30,
        speed: int = 200000,
        sleep_time: int = 2) -> OrderedPair:
    """
    Takes knob position as parameters to control the rotation of the motor and allow to control position
    and speed of a motor with a TIC driver
    """

    speed: int = speed
    sleep_time: int = sleep_time
    current_limit: int = current_limit

    # Converting the knob value into a position
    knob_position: int = 2 * knob_value

    # Declaration of the stepper driver (You can add serial number to specify the driver)
    tic: TicUSB = TicUSB()
    # Set the current limit for the driver TIC
    tic.set_current_limit(current_limit)
    tic.energize()  # Turn on the driver
    tic.exit_safe_start()  # The driver is now ready to receive commands
    # Set maximum speed for the motor during first movement.
    tic.set_max_speed(speed)

    tic.halt_and_set_position(0)  # Set initial position to origin
    sleep(sleep_time)

    # Set target position for the first movement
    tic.set_target_position(knob_position)
    sleep(sleep_time)

    tic.deenergize()
    tic.enter_safe_start()

    position_parameters = OrderedPair(x=knob_position, y=speed)

    return position_parameters
