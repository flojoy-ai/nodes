from flojoy import flojoy
import mecademicpy.robot as mdr


@flojoy
def Home(ConnHandle: mdr.Robot) -> mdr.Robot:
    """
    The Home node moves the robot arm to its home position.
    
    Inputs
    ------
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
        
    Returns
    -------
    mdr.Robot
        A handle to the robot arm object after it has been moved to the home position.
        
    """
    ConnHandle.Home()
    return ConnHandle
