import numpy as np
from flojoy import flojoy, DataContainer
from node_sdk.small_memory import SmallMemory

memory_key = 'sos-info'

@flojoy
def SECOND_ORDER_SYSTEM(v, params):
    # Let's first define things that won't change over
    # each iteration: time constants, etc ...
    d1 = float(params['d1']) #first time constant in us, 250
    d2 = float(params['d2']) #second time constant in us, 100
    node_id = params.get('node_id', 0)

    # ... and now some helper functions
    x1 = np.exp(-1.0 / d1) if d1 > 0 else 0.0
    x2 = np.exp(-1.0 / d2) if d2 > 0 else 0.0
    ac = (1.0 - x1) * (1.0 - x2)
    bpd = x1 + x2
    bd = x1 * x2

    # Now we require memory. The only thing we need in memory is the last two 
    # values the system had in this basic example.
    data = SmallMemory().read_memory(node_id, memory_key)
    if type(data) == dict:
        initialize = True
    elif type(data) == np.ndarray:
        initialize = False
    else:
        raise TypeError("Error loading object from REDIS.")
    
    y_primes = np.zeros((2,1)) if initialize else data
 
    # Using input from controller as v[0].y ...
    response = ac * v[0].y + bpd * y_primes[0] - bd * y_primes[1]
    y_primes[1] = y_primes[0]
    # we keep every bit of data. id-0 will still be the most recent
    # bit of data, and id-1 will still be the second most recent, so it works out
    # we do this so that we can pass it in reverse (earliest time first) to a visualization node
    # v['data'] = y_primes[::-1]

    y_primes = np.insert(y_primes, 0, response)
    print('-'*72+'\n'*5+f'Running iteration# {y_primes.size-1}' + ' , '+str([y for y in y_primes])+'\n'*5+'-'*72)
    # We now write to memory ...
    SmallMemory().write_to_memory(node_id, memory_key, y_primes)
    # ... and return the result!
    return DataContainer(x=v[0].y, y=float(y_primes[0])) #returns input output pair