import traceback
from flojoy import flojoy, DataContainer, JobResultBuilder
from typing import Union
import numpy as np
from PIL import Image
from os import path


@flojoy
def LOCAL_FILE(
    dc_inputs: list[DataContainer], params: dict
) -> Union[DataContainer, dict]:
    print("parameters passed to LOCAL_FILE: ", params)
    file_type = params["file_type"]
    match file_type:
        case "image":
            red_channel = []
            green_channel = []
            blue_channel = []
            alpha_channel = []
            try:
                default_image_path = path.join(
                    path.dirname(path.abspath(__file__)),
                    "assets",
                    "astronaut.png",
                )
                filePath = params["path"]
                if filePath == "":
                    filePath = default_image_path
                print(" file will be loaded from: ", filePath)
                f = Image.open(filePath)
                img_array = np.array(f.convert("RGBA"))
                if img_array.shape[2] == 4:
                    red_channel = img_array[:, :, 0]
                    green_channel = img_array[:, :, 1]
                    blue_channel = img_array[:, :, 2]
                    alpha_channel = img_array[:, :, 3]
                else:
                    red_channel = img_array[:, :, 0]
                    green_channel = img_array[:, :, 1]
                    blue_channel = img_array[:, :, 2]
                    alpha_channel = None
            except Exception:
                print(traceback.format_exc())
            return DataContainer(
                type="image",
                r=red_channel,
                g=green_channel,
                b=blue_channel,
                a=alpha_channel,
            )
        case _:
            return JobResultBuilder().from_inputs(dc_inputs).build()
