from flojoy import flojoy, display, DataContainer
from typing import Literal, Optional
from ticlib import TicUSB

tic = TicUSB()

current_limit_t500_dict = {
    "0": "0",
    "1": "1",
    "174": "2",
    "343": "3",
    "495": "4",
    "634": "5",
    "762": "6",
    "880": "7",
    "990": "8",
    "1092": "9",
    "1189": "10",
    "1281": "11",
    "1368": "12",
    "1452": "13",
    "1532": "14",
    "1611": "15",
    "1687": "16",
    "1762": "17",
    "1835": "18",
    "1909": "19",
    "1982": "20",
    "2056": "21",
    "2131": "22",
    "2207": "23",
    "2285": "24",
    "2366": "25",
    "2451": "26",
    "2540": "27",
    "2634": "28",
    "2734": "29",
    "2843": "30",
    "2962": "31",
    "3093": "32"
}

continuous_current_limit_dict = {
    "T500": "1500", 
    "T825": "1500", 
    "T834": "1500", 
    "T249": "1800", 
    "36v4": "4000"
}

unrestricted_current_limit_dict = {
    "T500": "3093", 
    "T825": "3456", 
    "T834": "3968", 
    "T249": "4480", 
    "36v4": "9095"
}

current_code_range_dict = {
    "T825": "125", 
    "T834": "125", 
    "T249": "125", 
    "36v4": "128"
}

current_increment_dict = {
    "T825": "32", 
    "T834": "32", 
    "T249": "40",
    "36v4": "71.615"
}
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


def create_current_dict(max_current_value, increment, code_range):
    """
    Create a dictionary of current values with corresponding keys.

    Parameters:
    -----------
    max_current_value : int
        The maximum current value.

    increment : int
        The increment between consecutive current values.

    code_range : int
        The code range where the current value should be replaced.

    Returns:
    --------
    dict
        A dictionary mapping current values to their corresponding keys.
    """
    current_dict = {str(i): i for i in range(0, max_current_value + increment, increment)}
    if str(max_current_value) in current_dict and int(code_range) < max_current_value:
        del current_dict[str(max_current_value)]
        current_dict[str(max_current_value)] = code_range
    return current_dict

def closest_value(compare_value, value_dict):
    closest_key = min(value_dict, key=lambda key: abs(value_dict[key] - compare_value))
    return value_dict[closest_key]


@flojoy(deps={"ticlib": "0.2.2", "pyusb": "1.2.1"})
def MOTOR_SETTINGS_TIC(
    default: Optional[DataContainer] = None,
    model: Literal["T500", "T825", "T834", "T249", "36v4", "T825"] = "T825",
    current_limit_mode: Literal["continuous_current_limit", "unrestricted_current_limit"] = "continuous_current_limit",
    current_limit_t500: int = 174,
    current_limit_t825: int = 192,
    current_limit_t834: int = 192,
    current_limit_t249: int = 200,
    current_limit_36v4: int = 215,
    step_mode_t500: Literal["Full", "1/2", "1/4", "1/8", "default"] = "default",
    step_mode_t825: Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "default"] = "default",
    step_mode_t834: Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "default"] = "default",
    step_mode_t249: Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "1/2 100%", "default"] = "default",
    step_mode_36v4: Literal["Full", "1/2", "1/4", "1/8", "1/16", "1/32", "1/64", "1/128", "1/256", "default"] = "default",
    decay_mode: int = 0,
    set_max_speed: int = 0,
    set_starting_speed: int = 0,
    set_max_acceleration: int = 0,
    set_max_deceleration: int = 0,

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

    current_limit_t500 : int, optional, units: mA
        Current limit for the Tic T500 model. Defaults to 0.

    current_limit_t825 : int, optional, units: mA
        Current limit for the Tic T825 model. Defaults to 0.

    current_limit_t834 : int, optional, units: mA
        Current limit for the Tic T834 model. Defaults to 0.

    current_limit_t249 : int, optional, units: mA
        Current limit for the Tic T249 model. Defaults to 0.

    current_limit_36v4 : int, optional, units: mA
        Current limit for the Tic 36v4 model. Defaults to 0.

    set_max_speed : int, optional, units: microsteps per 10,000 s
        The maximum speed setting. Defaults to 0.

    set_starting_speed : int, optional, units: microsteps per 10,000 s
        The starting speed setting. Defaults to 0.

    set_max_acceleration : int, optional, units: microsteps per 100 s²
        The acceleration setting. Defaults to 0.

    set_max_deceleration : int, optional, units: microsteps per 100 s²
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

    current_limit_model_dict = {
    "T500": current_limit_t500,
    "T825": current_limit_t825,
    "T834": current_limit_t834,
    "T249": current_limit_t249,
    "36v4": current_limit_36v4,
}   
    # Get product (model) name from settings
    parsed_settings = parse_settings(tic.settings.get_control_mode())["product"]
    
    # Define current_limit_dict
    if current_limit_mode == "continuous_current_limit":
        current_limit_dict = continuous_current_limit_dict
    else:
        current_limit_dict = unrestricted_current_limit_dict

    # Define increment, current_code_range, and max_current_value.
    increment = int(current_increment_dict[parsed_settings])
    current_code_range = int(current_code_range_dict[parsed_settings])
    max_current_value = int(current_limit_dict[parsed_settings])

    # Create the value_dict
    value_dict = create_current_dict(
        max_current_value=max_current_value,
        increment=increment,
        code_range=current_code_range,
    ) if parsed_settings != "T500" else current_limit_t500_dict

    # Set the current limit using closest_value.
    tic.set_current_limit(closest_value(compare_value=current_limit_model_dict[parsed_settings], value_dict=value_dict))

    # Get current limit
    current_limit = current_limit_dict.get(model)
    if model == parsed_settings and current_limit is not None:
        tic.set_current_limit(enforce_range(current_limit))

    # Step modes mapping
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

    # Set step mode
    for step_mode in [step_mode_t500, step_mode_t825, step_mode_t834, step_mode_t249, step_mode_36v4]:
        value = step_mode_dict.get(step_mode)
        if value is not None:
            tic.set_step_mode(value)
    
    tic.set_max_speed(enforce_range(set_max_speed, 0, 500000000))
    tic.set_starting_speed(enforce_range(set_starting_speed, 0, 500000000))
    tic.set_max_acceleration(enforce_range(set_max_acceleration, 100, 2147483647))
    tic.set_max_deceleration(enforce_range(set_max_deceleration, 100, 2147483647))


    return DataContainer

@display
def OVERLOAD(current_limit_t500, current_limit_mode, max_speed, starting_speed, acceleration, deceleration, decay_mode, step_mode_t500, model="T500") -> None:
    return None

@display
def OVERLOAD(current_limit_t825, current_limit_mode, max_speed, starting_speed, acceleration, deceleration, decay_mode, step_mode_t825, model="T825") -> None:
    return None

@display
def OVERLOAD(current_limit_t834, current_limit_mode, max_speed, starting_speed, acceleration, deceleration, decay_mode, step_mode_t834, model="T834") -> None:
    return None

@display
def OVERLOAD(current_limit_t249, current_limit_mode, max_speed, starting_speed, acceleration, deceleration, decay_mode, step_mode_t249, model="T249") -> None:
    return None

@display
def OVERLOAD(current_limit_36v4, current_limit_mode, max_speed, starting_speed, acceleration, deceleration, decay_mode, step_mode_36v4, model="36v4") -> None:
    return None
