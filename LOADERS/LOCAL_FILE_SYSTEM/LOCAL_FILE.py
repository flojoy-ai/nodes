from flojoy import flojoy, DataContainer, JobResultBuilder
from typing import Union
import numpy as np
from PIL import Image
from os import path


@flojoy
def LOCAL_FILE(
    dc_inputs: list[DataContainer], params: dict
) -> Union[DataContainer, dict]:
    """
    Load a local file and convert it to a DataContainer class.

    Args:
        dc_inputs (list[DataContainer]): List of input DataContainer objects.

        params (dict): `file_type` : type of file to load.

    Returns:
        DataContainer: The loaded file as a DataContainer class.

    Raises:
        Exception: If there is an error loading the file.

    Supported file types:
    - "image": Load an image file and return the RGB(A) channels as a DataContainer class.
    - Other file types: Return a DataContainer object with the same inputs.

    Note:
    - For the "image" file type, the path to the image file is specified in the 'path' parameter of 'params'.
      If 'path' is empty, a default image path will be used.

    """
    file_type: str = params["file_type"]
    filePath: str = params["path"]
    match file_type:
        case "image":
            try:
                default_image_path = path.join(
                    path.dirname(path.abspath(__file__)),
                    "assets",
                    "astronaut.png",
                )
                if filePath == "":
                    filePath = default_image_path
                print(" file will be loaded from: ", filePath)
                f = Image.open(filePath)
                img_array = np.array(f.convert("RGBA"))
                red_channel = img_array[:, :, 0]
                green_channel = img_array[:, :, 1]
                blue_channel = img_array[:, :, 2]
                if img_array.shape[2] == 4:
                    alpha_channel = img_array[:, :, 3]
                else:
                    alpha_channel = None
                return DataContainer(
                    type="image",
                    r=red_channel,
                    g=green_channel,
                    b=blue_channel,
                    a=alpha_channel,
                )
            except Exception as e:
                raise e
        case _:
            return JobResultBuilder().from_inputs(dc_inputs).build()
