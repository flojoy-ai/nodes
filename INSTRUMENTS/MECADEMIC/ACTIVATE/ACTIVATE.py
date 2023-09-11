from flojoy import flojoy
import mecademicpy.robot as mdr


@flojoy
def ActivateRobot(ConnHandle: mdr.Robot) -> mdr.Robot:
    """
    The ActivateRobot node activates the robot arm.
    
    Inputs
    ------
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
        
    Returns
    -------
    mdr.Robot
        A handle to the activated robot arm object.
        
    """
    ConnHandle.Activate()
    # Add verification step here
    return ConnHandle
