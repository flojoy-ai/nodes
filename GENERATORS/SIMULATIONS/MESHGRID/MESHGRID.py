from flojoy import flojoy, OrderedPair, Scalar
import numpy as np


@flojoy
def MESHGRID(x: Scalar, y: Scalar, nx: Scalar, ny: Scalar) -> OrderedPair:
    x_vec = np.linspace(0, x.c, int(nx.c))
    y_vec = np.linspace(0, y.c, int(ny.c))
    xv, yv = np.meshgrid(x_vec, y_vec)
    return OrderedPair(x=np.reshape(xv, -1), y=np.reshape(yv, -1))
