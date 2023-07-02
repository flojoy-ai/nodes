from flojoy import flojoy, DataContainer
from ticlib import TicUSB
from time import sleep


@flojoy
def STEPPER_DRIVER_TIC_KNOB(
    default: DataContainer,
    knob_value: int = 0,
    current_limit: int = 30,
    speed: int = 200000,
    sleep_time: int = 2,
) -> DataContainer:
    """
    Takes knob position as parameters to control the rotation of the motor and allow to control position
    and speed of a motor with a TIC driver
    """
    speed: int = params["speed"]
    sleep_time: int = params["sleep_time"]
    current_limit: int = params["current_limit"]
    knob_position: int = 2 * params["knob_value"]
    tic: TicUSB = TicUSB()
    tic.set_current_limit(current_limit)
    tic.energize()
    tic.exit_safe_start()
    tic.set_max_speed(speed)
    tic.halt_and_set_position(0)
    sleep(sleep_time)
    tic.set_target_position(knob_position)
    sleep(sleep_time)
    tic.deenergize()
    tic.enter_safe_start()
    return DataContainer(x={"a": knob_position, "b": knob_position}, y=knob_position)


@flojoy
def STEPPER_DRIVER_TIC_KNOB_MOCK(
    dc_inputs: list[DataContainer], params: dict
) -> DataContainer:
    """Mock function for the stepper driver node"""
    positions: list[int] = [50, 100, 150, 200]
    speeds: list[int] = [50000, 1000000, 150000, 200000]
    return DataContainer(x={"a": positions, "b": speeds}, y=positions)
