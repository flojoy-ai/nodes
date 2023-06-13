from os import path
import traceback
from flojoy import flojoy, DataContainer
from matplotlib import image
from numpy import asarray


@flojoy
def OPEN_IMAGE(dc_inputs: list[DataContainer], params: dict[str, str]) -> DataContainer:
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

    file_path = params["file_path"]
    if not path.exists(file_path):
        raise ValueError("File path does not exist!")
    read_image = image.imread(file_path)
    data = asarray(read_image)

    red_channel = data[:, :, 0]
    green_channel = data[:, :, 1]
    blue_channel = data[:, :, 2]

    if data.shape[2] == 4:
        alpha_channel = data[:, :, 3]
    else:
        alpha_channel = None
        
    return DataContainer(
        type="image",
        r=red_channel,
        g=green_channel,
        b=blue_channel,
        a=alpha_channel,
        )
