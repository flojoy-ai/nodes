from enum import Enum
from typing import Union

from flojoy import flojoy
import mecademicpy.robot as mdr


class IMecademicConnState(Enum):
    CONNECTED = "connected"
    LOADING = "loading"
    ERROR = "error"


@flojoy
def CONNECT(ip_address: str = '192.168.0.100') -> Union[IMecademicConnState, mdr.Robot]:
    """
    The CONNECT node establishes a connection to the Mecademic robot arm via its API.
    
    Outputs
    -------
    IMecademicConnState : Enum
        An enumerated type that represents the connection state. Possible states are 'connected', 'loading', and 'error'.
        
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
        
    """
    connection_state = IMecademicConnState.LOADING
    ConnHandle = mdr.Robot()
    try:
        ConnHandle.Connect(address=ip_address)
        if ConnHandle.IsConnected():
            connection_state = IMecademicConnState.CONNECTED
        else:
            connection_state = IMecademicConnState.ERROR
    except Exception as e:
        print(f"Connection error: {e}")
        connection_state = IMecademicConnState.ERROR
    return connection_state, ConnHandle
