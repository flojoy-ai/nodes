from flojoy import flojoy, DataContainer, Scalar
import mecademicpy.robot as mdr


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_JOINT_VEL(ConnHandle: DataContainer, v: Scalar) -> DataContainer:
    """
    The SET_JOINT_VEL node sets the arm's joint's velocity.
    
    Inputs
    ------
    ConnHandle : DataContainer
        A handle to the robot arm object.
    
    v : Scalar
        The cart velocity to be set.
    
    Returns
    -------
    ConnHandle
        A handle to the activated robot arm object.
        
    """
    if not ConnHandle.extra.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.extra.SetJointVel(v.c)
    return ConnHandle
