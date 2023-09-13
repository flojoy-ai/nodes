from flojoy import flojoy
import mecademicpy.robot as mdr


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_CART_LIN_VEL(ConnHandle: mdr.Robot, v: float) -> mdr.Robot:
    """
    The ActivateRobot node activates the robot arm.
    
    Inputs
    ------
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
    
    v : float
        The cart velocity to be set.
    
    Returns
    -------
    mdr.Robot
        A handle to the activated robot arm object.
        
    """
    if not ConnHandle.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.SetCartLinVel(v)
    return ConnHandle
