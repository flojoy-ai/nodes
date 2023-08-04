from flojoy import flojoy, Image, DataFrame
from typing import Literal
import numpy as np
from PIL import Image as PIL_Image
from os import path
import pandas as pd


def get_file_path(file_path: str, default_path: str | None = None):
    f_path = path.abspath(file_path) if file_path != "" else default_path
    if not f_path:
        raise ValueError("File path is missing for file_path parameter!")
    print(f"file will be loaded from {f_path}")
    return f_path


@flojoy(deps={"xlrd": "2.0.1", "lxml": "4.9.2", "openpyxl": "3.0.10"})
def LOCAL_FILE(
    file_path: str,
    file_type: Literal["Image", "JSON", "CSV", "Excel", "XML"] = "Image",
) -> Image | DataFrame:
    """The LOCAL_FILE node loads a local file of different type and converts it to a DataContainer class.

    Parameters
    ----------
    file_type : str
        type of file to load, default: image.
    file_path : str
        path to the file to be loaded.

    Returns:
    --------
    Image:
        type 'image' for file_type 'image'

        type 'dataframe' for file_type 'json', 'csv', 'excel', 'xml'

    """
    match file_type:
        case "Image":
            default_image_path = path.join(
                path.dirname(path.abspath(__file__)),
                "assets",
                "astronaut.png",
            )
            file_path = get_file_path(file_path, default_image_path)
            f = PIL_Image.open(file_path)
            img_array = np.array(f.convert("RGBA"))
            red_channel = img_array[:, :, 0]
            green_channel = img_array[:, :, 1]
            blue_channel = img_array[:, :, 2]
            if img_array.shape[2] == 4:
                alpha_channel = img_array[:, :, 3]
            else:
                alpha_channel = None
            return Image(
                r=red_channel,
                g=green_channel,
                b=blue_channel,
                a=alpha_channel,
            )
        case "CSV":
            file_path = get_file_path(file_path)
            df = pd.read_csv(file_path)
            return DataFrame(df=df)
        case "JSON":
            file_path = get_file_path(file_path)
            df = pd.read_json(file_path)
            return DataFrame(df=df)
        case "XML":
            file_path = get_file_path(file_path)
            df = pd.read_xml(file_path)
            return DataFrame(df=df)
        case "Excel":
            file_path = get_file_path(file_path)
            df = pd.read_excel(file_path)
            return DataFrame(df=df)
