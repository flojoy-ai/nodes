from flojoy import flojoy, Bytes, Scalar


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_JOINT_VEL(ConnHandle: Bytes, v: Scalar) -> Bytes:
    """
    The SET_JOINT_VEL node sets the robot arm's angular velocity for its joints.

    Inputs
    ------
    ConnHandle : Bytes
        A handle to the robot arm object.

    Parameters
    ------
    v : Scalar
        The angular velocity to be set for each joint.

    Returns
    -------
    ConnHandle
        A handle to the robot arm object after its joint velocity has been set.

    """
    if not ConnHandle.robot.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.robot.SetJointVel(v.c)
    return ConnHandle
