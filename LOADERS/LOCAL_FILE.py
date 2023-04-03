import traceback
from flojoy import flojoy,DataContainer, JobResultBuilder
import numpy as np
from PIL import Image

@flojoy
def LOCAL_FILE(v, params):
    print('parameters passed to LOCAL_FILE: ', params)
    red_channel = []
    green_channel = []
    blue_channel = []
    alpha_channel = []
    try:
        filePath = ''
        y = {}
        if v is not None and len(v) != 0:
            filePath = v[0].y
        ctrlInput = params['path']
        fileType = params['file_type']
        opType = params['op_type']
        if ctrlInput is not None and len(ctrlInput.strip()) > 0:
            filePath = ctrlInput
        elif len(filePath.strip()) == 0:
            if fileType == 'image' and opType == 'OD':
                filePath = "../public/assets/object_detection.png"
        print ("File to be loaded: " + filePath)
        f = Image.open(filePath)
        img_array = np.array(f)
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
    data_container = DataContainer(type = 'image',r=red_channel, g=green_channel, b=blue_channel, a=alpha_channel)

    return JobResultBuilder().from_data(data_container).to_plot(plot_type='image')
