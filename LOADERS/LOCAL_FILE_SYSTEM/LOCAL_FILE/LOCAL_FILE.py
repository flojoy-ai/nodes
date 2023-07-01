from flojoy import flojoy, DataContainer, JobResultBuilder, DefaultParams
from typing import Union
import numpy as np
from PIL import Image
from os import path
import pandas as pd


def get_file_path(file_path: str, default_path: str = None) -> str:
    if default_path is None and file_path == "":
        raise ValueError("File path is missing for file_path parameter!")
    f_path = file_path if file_path != "" else default_path
    print(f"file will be loaded from {f_path}")
    return f_path


@flojoy
def LOCAL_FILE(
    default: DataContainer,
    default_params: DefaultParams,
    file_type: Literal["image", "csv", "json", "xml", "excel"] = "image",
    path: str = "",
) -> Union[DataContainer, dict]:
    """The LOCAL_FILE node loads a local file of different type and converts it to a DataContainer class.

    Parameters
    ----------
    file_type : str
        type of file to load, default: image.
    file_path : str
        path to the file to be loaded.

    Returns:
    --------
    DataContainer:
        type 'image' for file_type 'image'

        type 'dataframe' for file_type 'json', 'csv', 'excel', 'xml'

    """
    file_type: str = params["file_type"]
    file_path: str = params["path"]
    match file_type:
        case "image":
            default_image_path = path.join(
                path.dirname(path.abspath(__file__)), "assets", "astronaut.png"
            )
            file_path = get_file_path(file_path, default_image_path)
            f = Image.open(file_path)
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
        case "csv":
            file_path = get_file_path(file_path)
            df = pd.read_csv(file_path)
            return DataContainer(type="dataframe", m=df)
        case "json":
            file_path = get_file_path(file_path)
            df = pd.read_json(file_path)
            return DataContainer(type="dataframe", m=df)
        case "xml":
            file_path = get_file_path(file_path)
            df = pd.read_xml(file_path)
            return DataContainer(type="dataframe", m=df)
        case "excel":
            file_path = get_file_path(file_path)
            df = pd.read_excel(file_path)
            return DataContainer(type="dataframe", m=df)
        case _:
            raise ValueError(
                f"LOCAL_FILE currently doesn't support file type : {file_type}"
            )
