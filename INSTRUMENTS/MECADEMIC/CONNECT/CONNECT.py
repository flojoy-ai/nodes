from flojoy import flojoy, node_initialization, NodeInitContainer, Bytes
import mecademicpy.robot as mdr


@flojoy(deps={"mecademicpy": "1.4.0"})
def CONNECT(init_container: NodeInitContainer) -> Bytes:
    """
    The CONNECT node establishes a connection to the Mecademic robot arm via its API.
    Returns
    -------
    Bytes
        Containing a handle to the robot arm object, which is connected, but not activated or homed.
    """
    ConnHandle = init_container.get()
    if ConnHandle.robot is None:
        raise ValueError("Robot communication is not open.")

    if not ConnHandle.robot.IsConnected():
        raise ValueError("Robot connection failed.")

    return Bytes(b=ConnHandle.b)


@node_initialization(for_node=CONNECT)
def init(address: str = '192.168.0.100') -> Bytes:
    robot: mdr.Robot = mdr.Robot()
    robot.Connect(address=address)
    return Bytes(robot=robot)
