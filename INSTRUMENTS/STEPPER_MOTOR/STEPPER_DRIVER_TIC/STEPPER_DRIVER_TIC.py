from flojoy import flojoy, DataContainer
from ticlib import (
    TicUSB,
)  # Import the TicUSB library to send command to Tic drivers with USB connection
from time import sleep


@flojoy
def STEPPER_DRIVER_TIC(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Takes current limit and sleep time as parameters and allow to control position
    and speed of a motor with a TIC driver
    """

    positions: list[int] = [50, 100, 150, 200]  # Setting default positions
    speeds: list[int] = [50000, 1000000, 150000, 200000]  # Setting default speeds
    current_limit: int = params["current_limit"]
    sleep_time: int = params["sleep_time"]

    # Declaration of the stepper driver
    tic: TicUSB = TicUSB()
    tic.halt_and_set_position(0)  # Set the position to 0
    tic.set_current_limit(current_limit)  # Set the current limit of the TIC driver
    tic.energize()  # Turn on the driver
    tic.exit_safe_start()  # The driver is now ready to receive commands

    for i in range(0, len(positions)):
        tic.set_max_speed(speeds[i])  # Set motor speed
        tic.set_target_position(positions[i])  # Set target positions
        sleep(sleep_time)

    tic.deenergize()
    tic.enter_safe_start()

    return DataContainer(x={"a": positions, "b": speeds}, y=positions)


@flojoy
def STEPPER_DRIVER_TIC_MOCK(
    dc_inputs: list[DataContainer], params: dict
) -> DataContainer:
    """Mock function for the stepper driver
    returns positions and speeds"""
    positions: list[int] = [50, 100, 150, 200]  # Setting default positions
    speeds: list[int] = [50000, 1000000, 150000, 200000]  # Setting default speeds

    return DataContainer(x={"a": positions, "b": speeds}, y=speeds)
