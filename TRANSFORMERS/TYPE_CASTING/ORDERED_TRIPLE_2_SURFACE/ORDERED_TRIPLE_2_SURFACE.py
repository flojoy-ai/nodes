from flojoy import flojoy, OrderedTriple, Surface
import numpy as np


@flojoy
def OrderedTriple_2_SURFACE(default: OrderedTriple) -> Surface:
    """The OrderedTriple_2_SURFACE node takes `OrderedTriple` instance of DataContainer class containing three arrays: x, y, and z.
    It reshapes the z array into a 2D grid using the unique values of x and y.
    The resulting 2D grid is used to create a Surface object with corresponding x, y, and z values.

    Parameters:
    ------------
    None

    Returns:
    `Surface`

    """
    x = np.unique(default.x)
    y = np.unique(default.y)

    z_size = len(x) * len(y)

    # Truncate or pad the z array to match the desired size
    if z_size > len(default.z):
        z = np.pad(default.z, (0, z_size - len(default.z)), mode="constant").reshape(
            len(y), len(x)
        )
    else:
        z = default.z[:z_size].reshape(len(y), len(x))

    X, Y = np.meshgrid(x, y)
    return Surface(x=X, y=Y, z=z)
