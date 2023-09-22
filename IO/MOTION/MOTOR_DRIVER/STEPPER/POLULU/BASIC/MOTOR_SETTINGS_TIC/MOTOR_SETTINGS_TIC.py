from flojoy import flojoy, display, DataContainer
from typing import Literal, Optional
from ticlib import TicUSB

tic = TicUSB()

def parse_settings(settings_text: str):
    """
    Parse settings from the provided settings text.

    Parameters:
    ----------
    settings_text : str
        The text containing settings data.

    Returns:
    -------
    dict
        A dictionary containing the parsed key-value pairs.
    """
    return dict(line.strip().split(": ", 1) for line in settings_text.strip().split("\n"))

def enforce_range(input_value: int, min_value: int, max_value: int):
    """
    Enforce that the input value falls within the specified range.

    Parameters:
    -----------
        input_value, int:
            The value to be checked.

        min_value, int:
            The minimum allowed value.

        max_value, int:
            The maximum allowed value.

    Returns:
    --------
        int:
            The input_value if it is within the specified range.

    Raises:
    -------
        ValueError: If the value is outside the specified range.
    """
    if min_value <= input_value <= max_value:
        return input_value
    raise ValueError(
        f"Value {input_value} is outside the allowed range from {min_value} to {max_value}."
    )

# def enforce_current_limit():
#     """
#     Get Tic stepper driver model.
#     Compare model to list
#     Use closest valid setting for current, (e.i: 900 mA -> 1500/124 % 900)
#     """
#     parsed_settings = parse_settings(tic.settings.get_control_mode())
#     parsed_settings["product"]

@flojoy(deps={"ticlib": "0.2.2", "pyusb": "1.2.1"})
def MOTOR_SETTINGS_TIC(
    default: Optional[DataContainer] = None,
    model: Literal["T500", "T825", "T834", "T249", "36v4", "T825"] = "T825",
    current_limit_t500: int = 0,
    current_limit_t825: int = 0,
    current_limit_t834: int = 0,
    current_limit_t249: int = 0,
    current_limit_36v4: int = 0,
    max_speed: int = 2000000,
    starting_speed: int = 1000000,
    acceleration: int = 40000,
    deceleration: int = 0,
    step_mode_t500: Literal["Full", "1/2", "1/4", "1/8", "default"] = "default",
    step_mode_t825: Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "default"] = "default",
    step_mode_t834: Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "default"] = "default",
    step_mode_t249: Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "1/2 100%", "default"] = "default",
    step_mode_36v4: Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "1/64", "1/128", "1/256", "default"] = "default",
    decay_mode: int = 0,
) -> DataContainer:
    
    """
    Configure settings for a Tic T-series stepper driver.

    This function allows you to configure various settings for a Pololu Tic T-series stepper driver, including model selection, current limits,
    speed settings, step modes, and more.
    
    Parameters
    ----------
    default : DataContainer
        The default data container.

    model : Literal["T500", "T825", "T834", "T249", "36v4", "T825"], optional
        The Tic model to configure. Defaults to "T825".

    current_limit_t500 : int, optional
        Current limit for the Tic T500 model. Defaults to 0.

    current_limit_t825 : int, optional
        Current limit for the Tic T825 model. Defaults to 0.

    current_limit_t834 : int, optional
        Current limit for the Tic T834 model. Defaults to 0.

    current_limit_t249 : int, optional
        Current limit for the Tic T249 model. Defaults to 0.

    current_limit_36v4 : int, optional
        Current limit for the Tic 36v4 model. Defaults to 0.

    max_speed : int, optional
        The maximum speed setting. Defaults to 2000000.

    starting_speed : int, optional
        The starting speed setting. Defaults to 1000000.

    acceleration : int, optional
        The acceleration setting. Defaults to 40000.

    deceleration : int, optional
        The deceleration setting. Defaults to 0.

    step_mode_t500 : Literal["Full", "1/2", "1/4", "1/8", "default"], optional
        The step mode for the Tic T500 model. Defaults to "default".

    step_mode_t825 : Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "default"], optional
        The step mode for the Tic T825 model. Defaults to "default".

    step_mode_t834 : Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "default"], optional
        The step mode for the Tic T834 model. Defaults to "default".

    step_mode_t249 : Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "1/2 100%", "default"], optional
        The step mode for the Tic T249 model. Defaults to "default".

    step_mode_36v4 : Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "1/64", "1/128", "1/256", "default"], optional
        The step mode for the Tic 36v4 model. Defaults to "default".

    decay_mode : int, optional
        The decay mode setting. Defaults to 0.

    Returns
    -------
    DataContainer
        Returns empty DataContainer.
    """
    step_modes = [step_mode_t500, step_mode_t825, step_mode_t834, step_mode_t249, step_mode_36v4]

    step_mode_dict = {
        "Full": 0,
        "1/2": 1,
        "1/4": 2,
        "1/8": 3,
        "1/16": 4,
        "1/32": 5,
        "1/2 100%": 6,
        "1/64": 7,
        "1/128": 8,
        "1/256": 9,
        "default": None
    }

    for step_mode in step_modes:
        if step_mode != "default":
            value = step_mode_dict.get(step_mode)
            tic.set_step_mode(value)

    return DataContainer

@display
def OVERLOAD(current_limit_t500, max_speed, starting_speed, acceleration, deceleration, step_mode_t500, model="T500") -> None:
    return None

@display
def OVERLOAD(current_limit_t825, max_speed, starting_speed, acceleration, deceleration, step_mode_t825, model="T825") -> None:
    return None

@display
def OVERLOAD(current_limit_t834, max_speed, starting_speed, acceleration, deceleration, step_mode_t834, model="T834") -> None:
    return None

@display
def OVERLOAD(current_limit_t249, max_speed, starting_speed, acceleration, deceleration, step_mode_t249, model="T249") -> None:
    return None

@display
def OVERLOAD(current_limit_36v4, max_speed, starting_speed, acceleration, deceleration, step_mode_36v4, model="36v4") -> None:
    return None
