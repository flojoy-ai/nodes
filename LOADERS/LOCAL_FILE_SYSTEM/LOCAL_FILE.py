import traceback
from flojoy import flojoy,DataContainer, JobResultBuilder
import numpy as np
from PIL import Image
from os import path

@flojoy
def LOCAL_FILE(v, params):
    print('parameters passed to LOCAL_FILE: ', params)
    file_type = params.get('file_type', 'image')
    match file_type:
        case 'image':       
            red_channel = []
            green_channel = []
            blue_channel = []
            alpha_channel = []
            try:
                filePath = ''
                ctrlInput = params['path']
                opType = params['op_type']
                if ctrlInput is not None and len(ctrlInput.strip()) > 0:
                    filePath = ctrlInput
                elif len(filePath.strip()) == 0:
                    if opType == 'OD':
                        filePath = path.join(path.dirname(path.abspath(__file__)), "assets", "object_detection.png")
                print ("File to be loaded: " + filePath)
                f = Image.open(filePath)
                img_array = np.array(f.convert('RGBA'))
                if img_array.shape[2] == 4:
                    red_channel = img_array[:,:,0]
                    green_channel = img_array[:,:,1]
                    blue_channel = img_array[:,:,2]
                    alpha_channel = img_array[:,:,3]
                else:
                    red_channel = img_array[:,:,0]
                    green_channel = img_array[:,:,1]
                    blue_channel = img_array[:,:,2]
                    alpha_channel = None
            except Exception:
                print(traceback.format_exc())
            return DataContainer(type = 'image',r=red_channel, g=green_channel, b=blue_channel, a=alpha_channel)
        case _:
            return JobResultBuilder().from_inputs(v).build()
