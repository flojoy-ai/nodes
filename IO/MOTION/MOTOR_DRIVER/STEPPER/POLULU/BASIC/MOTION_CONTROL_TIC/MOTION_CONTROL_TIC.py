from flojoy import flojoy, DataContainer
from typing import Literal, Optional
from ticlib import TicUSB

tic = TicUSB()

tic.get_current_position()

def enforce_range(input_value: int, min_value: int, max_value: int):
    # """
    # Enforce that the input value falls within the specified range.

    # Parameters
    # ----------
    #     input_value, int:
    #         The value to be checked.

    #     min_value, int:
    #         The minimum allowed value.

    #     max_value, int:
    #         The maximum allowed value.

    # Returns
    # -------
    #     int:
    #         The input_value if it is within the specified range.

    # Raises
    # ------
    #     ValueError: If the value is outside the specified range.
    # """
    if min_value <= input_value <= max_value:
        return input_value
    raise ValueError(
        f"Value {input_value} is outside the allowed range from {min_value} to {max_value}."
    )


def enforce_limit_switches(go_home: str):
    # """
    # Check the availability of limit switches for the selected homing direction.

    # Parameters
    # ----------
    # go_home : str
    #     Specifies the homing direction.

    #     Options:
    #     - "forward"
    #     - "reverse"

    # Returns
    # -------
    # int
    #     1 if compatible limit switches are properly set.

    # Raises
    # ------
    # Exception:
    #     Limit switches not available for the selected homing direction.
    # """

    switch_types = ["scl", "sda", "tx", "rx", "rc"]

    for switch_type in switch_types:
        setting_name = f"get_{switch_type}_limit_switch_{go_home}"
        errors = []

        try:
            if getattr(tic.settings, setting_name)() != 1:
                errors.append(Exception(f"Limit switch {switch_type} is not properly set for {go_home} homing direction."))
        except Exception as e:
            errors.append(e)

    for error in errors:
        raise error

    return 1


@flojoy(deps={"ticlib": "0.2.2", "pyusb": "1.2.1"})
def MOTION_CONTROL_TIC(
    default: Optional[DataContainer] = None,
    power_control: Literal["energize", "de-energize", "default"] = "default",
    halt_and_hold: bool = False,
    halt_and_set_position: int = 0,
    set_target_position: int = 0,
    set_target_velocity: int = 0,
    go_home: Literal["forward", "reverse", "default"] = "default",
) -> DataContainer:
    """
    Controls motion for a Pololu Tic T-series stepper driver.

    This function allows you to control the motion of a stepper motor using a Pololu Tic T-series stepper driver. It provides options for powering the motor, setting positions and velocities, and performing actions like halting and homing.

    Compatible with the Pololu Tic T500, T249, T825, T834, and T36v4 stepper drivers.

    For more details on usage, see the Tic Stepper Motor Controller User's Guide:
    https://www.pololu.com/docs/0J71/8

    Parameters
    ----------
    default : DataContainer
        The default data container.

    power_control : str, optional
        Control the motor's power state. Options: "energize" to power the motor, "de-energize" to stop powering it, or "default" to maintain the current power state.

    halt_and_hold : bool, optional
        If set to True, the motor will halt and maintain its current position.

    halt_and_set_position : int, optional, units: microsteps
        Set the motor's position when it comes to a halt.

    set_target_position : int, optional, units: microsteps
        Set the target position for the motor.

    set_target_velocity : int, optional, units: microsteps per 10,000 seconds
        Set the target velocity for the motor.

    go_home : bool, optional
        When True, the motor will execute a homing operation. Can only be used if limit switches have been enabled.

    Returns
    -------
    DataContainer
        Returns empty DataContainer.
    """

    if power_control == "energize":
        tic.energize()
    elif power_control == "de-energize":
        tic.deenergize()

    tic.halt_and_set_position(
        enforce_range(halt_and_set_position, -2147483648, 2147483647)
    )

    tic.set_target_position(enforce_range(set_target_position, -2147483648, 2147483647))

    tic.set_target_velocity(enforce_range(set_target_velocity, -500000000, 500000000))

    if halt_and_hold == True:
        tic.halt_and_hold()

    if go_home in ["forward", "reverse"]:
        tic.go_home(enforce_limit_switches(go_home))

    return DataContainer
