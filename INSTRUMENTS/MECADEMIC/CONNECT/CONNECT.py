from flojoy import flojoy, node_initialization, NodeInitContainer, MecademicConnHandle
import mecademicpy.robot as mdr
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def CONNECT(init_container: NodeInitContainer) -> MecademicConnHandle:
    """
    The CONNECT node establishes a connection to the Mecademic robot arm via its API.
    Returns
    -------
    MecademicConnHandle
        Containing a handle to the robot arm object, which is connected, but not activated or homed.
    """
    conn_handle: MecademicConnHandle = init_container.get()
    check_connection(conn_handle.robot)
    return conn_handle


@node_initialization(for_node=CONNECT)
def init(address: str = '192.168.0.100') -> MecademicConnHandle:
    robot: mdr.Robot = mdr.Robot()
    robot.Connect(address=address)
    return MecademicConnHandle(robot=robot)
