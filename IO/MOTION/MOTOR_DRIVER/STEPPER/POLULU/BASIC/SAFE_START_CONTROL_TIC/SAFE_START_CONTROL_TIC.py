from flojoy import flojoy, DataContainer
from typing import Literal
from ticlib import TicUSB

tic = TicUSB()

@flojoy(deps={"ticlib": "0.2.2", "pyusb": "1.2.1"})
def SAFE_START_CONTROL_TIC(
    default: DataContainer,
    safe_start_control: Literal[
        "enter_safe_start", "exit_safe_start"
    ] = "exit_safe_start",
) -> DataContainer:
    """
    Controls the safe start feature of the Pololu Tic T-series stepper drivers.

    This function allows you to start or stop the motor using the safe start feature of the Tic stepper driver. The safe start feature helps prevent accidental motor motion and can be used to clear safe start errors or enable safe start violations.

    Compatible with the Pololu Tic T500, T249, T825, T834, and T36v4 stepper drivers.

    For more details on usage, see the Tic Stepper Motor Controller User's Guide:
    https://www.pololu.com/docs/0J71/8

    Inputs
    ------
    default : DataContainer, optional
        Default is None.

    Parameters
    ----------
    safe_start_control : str
        Specifies the safe start action.

        Options:
        
        - "enter_safe_start" to enable the "safe start violation" error and halt the motor.

        - "exit_safe_start" to clear the "safe start violation" error and allow the motor to start up.

    Returns
    -------
    DataContainer
        Returns empty DataContainer.

    """


    if safe_start_control == "enter_safe_start":
        tic.enter_safe_start()
    else:
        tic.exit_safe_start()

    return DataContainer
