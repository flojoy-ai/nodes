from flojoy import flojoy, JobResultBuilder, DataContainer
import os
from redis import Redis
from rq.job import Job, NoSuchJobError
import traceback
from node_sdk.small_memory import SmallMemory
import numpy as np

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)

@flojoy
def LINE(v, params):
    referred_node = params['referred_node']
    x = v[0].y
    if referred_node is not '':
        referred_node_key = referred_node.split('-')[0]
        try:
            job = Job.fetch(referred_node, connection=Redis(
            host=REDIS_HOST, port=REDIS_PORT))
            y = SmallMemory().read_memory(job.get_id(), referred_node_key)
            print('-'*72+'\n'*5+f'{y.size-1} iterations' + f' for {referred_node_key} , '+str([i for i in y])+'\n'*5+'-'*72)

        except (Exception, NoSuchJobError):
            y = v[0].y if len(v) > 0 else [1, 3, 2]
            print(traceback.format_exc())
            pass
        return JobResultBuilder().from_inputs([DataContainer(x=np.arange(0,len(y),1),y=y)]).build()
    else:
        return JobResultBuilder().from_inputs(v).to_plot(plot_type='line')

