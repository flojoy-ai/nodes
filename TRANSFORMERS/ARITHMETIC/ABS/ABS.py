import numpy as np
from flojoy import flojoy, DataContainer

@flojoy
def ABS(v, params):
    ''' Returns abolute value '''
    return DataContainer(x=v[0].y, y=np.abs(v[0].y))