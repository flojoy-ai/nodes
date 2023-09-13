from flojoy import flojoy, Array
import mecademicpy.robot as mdr


@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_JOINTS(
    ConnHandle: mdr.Robot, 
    joint_angles: Array
) -> mdr.Robot:
    """
    The MOVE_JOINTS node moves the robot arm joints to the specified angles.
    
    Inputs
    ------
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
        
    joint_angles : Array
        Array of desired joint angles in degrees.
        
    Returns
    -------
    mdr.Robot
        A handle to the robot arm object after the joints have been moved.
        
    """
    if not ConnHandle.IsConnected():
        raise ValueError("Robot connection failed.")

    ConnHandle.MoveJoints(*joint_angles)
    return ConnHandle
