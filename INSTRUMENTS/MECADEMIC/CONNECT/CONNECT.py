from flojoy import flojoy, node_initialization, NodeInitContainer, DataContainer
import mecademicpy.robot as mdr


@flojoy(deps={"mecademicpy": "1.4.0"})
def CONNECT(init_container: NodeInitContainer) -> DataContainer:
    """
    The CONNECT node establishes a connection to the Mecademic robot arm via its API.
    """
    robot_container = init_container.get()
    if robot_container.extra is None:
        raise ValueError("Robot communication is not open.")

    if not robot_container.extra.IsConnected():
        raise ValueError("Robot connection failed.")
    
    return DataContainer(type='Bytes', extra=robot_container.extra)


@node_initialization(for_node=CONNECT)
def init(
    address: str = '192.168.0.100',
    enable_synchronous_mode: bool = False,
    disconnect_on_exception: bool = True,
    monitor_mode: bool = False,
    offline_mode: bool = False,
    timeout: float = 1
) -> DataContainer:
    ConnState: mdr.Robot = mdr.Robot()

    # Open Robot Com
    ConnState.Connect(
        address=address,
        enable_synchronous_mode=enable_synchronous_mode,
        disconnect_on_exception=disconnect_on_exception,
        monitor_mode=monitor_mode,
        offline_mode=offline_mode,
        timeout=timeout,
    )

    return DataContainer(type='Bytes', extra=ConnState)
