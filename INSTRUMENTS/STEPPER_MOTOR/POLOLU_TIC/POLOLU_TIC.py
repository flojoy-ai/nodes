from flojoy import (
    flojoy, 
    OrderedPair,
    Optional, 
    OrderedPair,
    DefaultParams,
    SmallMemory,
)
from ticlib import TicUSB
from time import sleep

MEMORY_KEY = "POLOLU_TIC_MEMORY_KEY"

tic = TicUSB()

@flojoy(inject_node_metadata=True, deps={"ticlib": "0.2.2", "pyusb": "1.2.1"})
def POLOLU_TIC(
    default_params: DefaultParams,
    previous_position: Optional[OrderedPair] = None,
    current_position: int = 0,
    target_position: int = 300,
) -> OrderedPair:
    """
    The POLOLU_TIC node allows you to set starting and target positions of a stepper
    motor compatible with the Pololu Tic T500, T249, T825, T834 and T36v4 stepper drivers.
    It returns time elapsed until target position is reached.

    Inputs
    ------
    default : OrderedPair
        Optional input to use as the current position. Default is None.

    Parameters
    ----------
    current_position : int
        set current stepper motor position. Default is 0.
    target_position : int
        set target stepper motor position. Default is 0.
    
    Returns
    -------
    OrderedPair
        x: current stepper motor position
        y: the amount of time in milliseconds until target position is reached
    """

    job_id = default_params.job_id
    previous_position = SmallMemory().read_memory(job_id, MEMORY_KEY)

    tic.energize()
    tic.exit_safe_start()
    tic.halt_and_set_position(previous_position if previous_position != None else current_position)
    tic.set_current_limit(34)
    tic.set_decay_mode(0)
    tic.set_max_acceleration(40000)
    tic.set_max_deceleration(0)
    tic.set_max_speed(2000000)
    tic.set_starting_speed(500000)
    tic.set_step_mode(0)
    tic.set_target_position(target_position)

    # time_since_last_step = tic.get_time_since_last_step() / 1000

    while tic.get_current_position() != tic.get_target_position():
        sleep(0.1)

    tic.deenergize()
    tic.enter_safe_start()

    final_position = tic.get_current_position()

    SmallMemory().write_to_memory(job_id, MEMORY_KEY, str(previous_position))

    x=current_position
    y=final_position

    # match default:
    #     case OrderedPair():
    #         return OrderedPair(x=current_position, y=int(final_position))
        
    return OrderedPair(x=x, y=y)