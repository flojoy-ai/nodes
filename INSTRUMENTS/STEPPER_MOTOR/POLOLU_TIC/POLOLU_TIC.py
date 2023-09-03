from flojoy import flojoy, OrderedPair
from ticlib import TicUSB
from time import sleep

tic = TicUSB()


@flojoy(deps={"ticlib": "0.2.2", "pyusb": "1.2.1"})
def POLOLU_TIC(initial_position: int = 0, target_position: int = 0, delay: float = 0.2) -> OrderedPair:
    """
    The POLOLU_TIC node allows you to set starting and target positions of a stepper
    motor compatible with the Pololu Tic T500, T249, T825, T834 or T36v4 stepper drivers.
    It returns time elapsed until target position is reached.

    Parameters
    ----------
    initial_position : int
        set current stepper motor position. Default is 0.
    target_position : int
        set target stepper motor position. Default is 0.
    delay: float
        set time buffer of time so that motor can move between initial and target position.

    Returns
    -------
    OrderedPair
        x: current stepper motor position
        y: the amount of time in milliseconds until target position is reached

    """
    tic.energize()
    tic.exit_safe_start()

    tic.halt_and_set_position(initial_position)
    tic.set_current_limit(32)
    tic.set_decay_mode(0)
    tic.set_max_acceleration(40000)
    tic.set_max_deceleration(0)
    tic.set_max_speed(200000)
    tic.set_starting_speed(180000)
    tic.set_step_mode(0)
    tic.set_target_position(target_position)

    time_since_last_step = tic.get_time_since_last_step() / 1000

    sleep(delay)

    tic.deenergize()
    tic.enter_safe_start()

    return OrderedPair(x=initial_position, y=time_since_last_step)
