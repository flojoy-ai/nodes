from flojoy import flojoy
from typing import Optional
import mecademicpy.robot as mdr


@flojoy
def MoveLin(
    ConnHandle: mdr.Robot, 
    x: float, 
    y: float, 
    z: float, 
    alpha: Optional[float] = None, 
    beta: Optional[float] = None, 
    gamma: Optional[float] = None
) -> mdr.Robot:
    """
    The MoveLin node linearly moves the robot's tool to an absolute Cartesian position.
    
    Inputs
    ------
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
        
    x, y, z : float
        Desired end effector coordinates in mm.
        
    alpha, beta, gamma : Optional[float]
        Desired end effector orientation in degrees. Optional and may be omitted for 4-axes robots.
        
    Returns
    -------
    mdr.Robot
        A handle to the robot arm object after it has been moved.
        
    """
    ConnHandle.MoveLin(x, y, z, alpha, beta, gamma)
    return ConnHandle