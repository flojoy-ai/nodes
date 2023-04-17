import traceback
from flojoy import flojoy, DataContainer, JobResultBuilder
import numpy as np

from utils.object_detection.object_detection import detect_object


@flojoy
def OBJECT_DETECTION(v, params):
    try:
        red_channel = []
        green_channel = []
        blue_channel = []
        alpha_channel = []
        print('Detecting objects...')
        r = v[0].r
        g = v[0].g
        b = v[0].b
        a = v[0].a
        print(" a here: ", a)
        if a is not None:
            nparr = np.stack((r, g, b, a), axis=2)
        else:
            nparr = np.stack((r, g, b), axis=2)
        img_array = detect_object(nparr)
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
        return DataContainer(type = 'image',r=red_channel, g=green_channel, b=blue_channel, a=alpha_channel)
    
    except Exception:
        print(traceback.format_exc())
        raise
