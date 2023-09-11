from enum import Enum
import time
from typing import Union

from flojoy import flojoy
import mecademicpy.robot as mdr


class IMecademicConnState(Enum):
    CONNECTED = "connected"
    LOADING = "loading"
    ERROR = "error"


@flojoy
def Connection() -> Union[IMecademicConnState, mdr.Robot]:
    """
    The Connection node establishes a connection to the Mecademic robot arm via its API.
    
    Outputs
    -------
    IMecademicConnState : Enum
        An enumerated type that represents the connection state. Possible states are 'connected', 'loading', and 'error'.
        
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
        
    """
    
    # Initialize connection state as LOADING
    connection_state = IMecademicConnState.LOADING
    
    # Initialize robot handle
    ConnHandle = mdr.Robot()
    
    # Try to connect to the robot
    try:
        ConnHandle.Connect(address='192.168.0.100')
        
        # Allow time for the connection to be established
        # TODO: This delay is arbitrary. Ideally, a callback or event should signal when the connection is established.
        time.sleep(2)  # Wait for 2 seconds as an example
        
        # Check if connected
        if ConnHandle.IsConnected():
            connection_state = IMecademicConnState.CONNECTED
        else:
            connection_state = IMecademicConnState.ERROR
            
    except Exception as e:
        # An exception occurred, set state to ERROR
        connection_state = IMecademicConnState.ERROR
    
    return connection_state, ConnHandle
