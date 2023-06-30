from os import path
import traceback
from flojoy import flojoy, DataContainer, DefaultParams
from matplotlib import image
from numpy import asarray

@flojoy
def OPEN_IMAGE(default: DataContainer, default_parmas: DefaultParams, file_path: str='') -> DataContainer:
    """
    The OPEN_IMAGE node loads an image file from disk and
    returns a image type Datacontainer object.

    Parameters
    ----------
    file_path : str
        path to the file to be loaded.

    Returns:
    --------
    DataContainer:
        type 'image', r, g, b , a
    """
    if not path.exists(file_path):
        raise ValueError('File path does not exist!')
    read_image = image.imread(file_path)
    data = asarray(read_image)
    red_channel = data[:, :, 0]
    green_channel = data[:, :, 1]
    blue_channel = data[:, :, 2]
    if data.shape[2] == 4:
        alpha_channel = data[:, :, 3]
    else:
        alpha_channel = None
    return DataContainer(type='image', r=red_channel, g=green_channel, b=blue_channel, a=alpha_channel)