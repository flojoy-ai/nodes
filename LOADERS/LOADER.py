from flojoy import flojoy, JobResultBuilder
from flojoy.utils import PlotlyJSONEncoder
import os
import requests
import json
from pathlib import Path
import yaml
from datetime import datetime

FRONTIER_HOST= os.environ.get('FRONTIER_HOST')
FORNTIER_PORT = os.environ.get('FRONTIER_PORT')
API_URI= f"https://{FRONTIER_HOST}:{FORNTIER_PORT}/measurements"


@flojoy
def LOADER(v, params):
    api_key = get_api_key()
    measurement_uuid = params['measurement_uuid']
    
    if api_key != '' and measurement_uuid != '':
        requests.post(f'{API_URI}/{measurement_uuid}', 
                      json={'api_key':api_key, 
                            'measurements': json.dumps({'data':v}, cls=PlotlyJSONEncoder),
                            'time': datetime.now().__str__()})
        return JobResultBuilder().from_inputs(v).build()
    else:
        not_found_key = 'FRONTIER_API_KEY' if api_key is '' else 'Measurement UUID'
        raise KeyError(f'{not_found_key} not found!')


def get_api_key():
    home = str(Path.home())
    api_key = ''
    path = os.path.join(home, '.flojoy/credentials')
    if not os.path.exists(path):
        return api_key
    
    stream = open(path, 'r')
    yaml_dict = yaml.load(stream, Loader=yaml.FullLoader)
    if isinstance(yaml_dict, str) == True:
        split_by_line = yaml_dict.split('\n')
        for line in split_by_line:
            if 'FRONTIER_API_KEY' in line:
                api_key = line.split(':')[1]
    else:
        api_key = yaml_dict['FRONTIER_API_KEY']
    return api_key