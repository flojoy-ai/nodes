from flojoy import flojoy
import mecademicpy.robot as mdr


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_JOINT_VEL(ConnHandle: mdr.Robot, p: float) -> mdr.Robot:
    """
    The SET_JOINT_VEL node sets the robot arm's joint velocity.
    
    Inputs
    ------
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
    
    p : float
        The cart velocity to be set.
    
    Returns
    -------
    mdr.Robot
        A handle to the activated robot arm object.
        
    """
    if not ConnHandle.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.SetJointVel(p)
    return ConnHandle
