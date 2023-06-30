from flojoy import flojoy, DataContainer, DefaultParams
from ticlib import TicUSB
from time import sleep

@flojoy
def STEPPER_DRIVER_TIC(default: DataContainer, default_parmas: DefaultParams, current_limit: int=30, sleep_time: int=2) -> DataContainer:
    """
    Takes current limit and sleep time as parameters and allow to control position
    and speed of a motor with a TIC driver
    """
    positions: list[int] = [50, 100, 150, 200]
    speeds: list[int] = [50000, 1000000, 150000, 200000]
    current_limit: int = params['current_limit']
    sleep_time: int = params['sleep_time']
    tic: TicUSB = TicUSB()
    tic.halt_and_set_position(0)
    tic.set_current_limit(current_limit)
    tic.energize()
    tic.exit_safe_start()
    for i in range(0, len(positions)):
        tic.set_max_speed(speeds[i])
        tic.set_target_position(positions[i])
        sleep(sleep_time)
    tic.deenergize()
    tic.enter_safe_start()
    return DataContainer(x={'a': positions, 'b': speeds}, y=positions)

@flojoy
def STEPPER_DRIVER_TIC_MOCK(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Mock function for the stepper driver
    returns positions and speeds"""
    positions: list[int] = [50, 100, 150, 200]
    speeds: list[int] = [50000, 1000000, 150000, 200000]
    return DataContainer(x={'a': positions, 'b': speeds}, y=speeds)