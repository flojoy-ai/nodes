from flojoy import flojoy
import mecademicpy.robot as mdr


@flojoy(deps={"mecademicpy": "1.4.0"})
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
    if not ConnHandle.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.Activate()
    return ConnHandle
