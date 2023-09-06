from flojoy import flojoy, Image, DataFrame, Grayscale, TextBlob
from typing import Literal, Optional
import numpy as np
from PIL import Image as PIL_Image
from os import path
import pandas as pd


def get_file_path(file_path: str, default_path: str | None = None):
    f_path = path.abspath(file_path) if file_path != "" else default_path
    if not f_path:
        raise ValueError(
            "The file path of the input file is missing. "
            "Please provide a input TextBlob or a provide `file_path` with a value!"
        )
    return f_path


@flojoy(
    deps={
        "xlrd": "2.0.1",
        "lxml": "4.9.2",
        "openpyxl": "3.0.10",
        "scikit-image": "0.21.0",
    }
)
def LOCAL_FILE(
    file_path: str = None,
    default: Optional[TextBlob] = None,
    file_type: Literal["Image", "Grayscale", "JSON", "CSV", "Excel", "XML"] = "Image",
) -> Image | DataFrame:
    """The LOCAL_FILE node loads a local file of a different type and converts it to a DataContainer class.

    Parameters
    ----------
    file_path : str
        path to the file to be loaded
    default   : Optional[TextBlob]
        If this input node is connected, the filename will be taken from
        the output of the connected node. To be used in conjunction with batch processing
    file_type : str
        type of file to load, default = image

    Notes
    -----
    If both file_path and default are not specified when `file_type="Image"`, a default image will be loaded.

    Raises
    ------
    ValueError
        If the file path is not specified and the default input is not connected, a ValueError is raised.

    Returns
    -------
    Image|DataFrame
        Image for file_type 'image'
        DataFrame for file_type 'json', 'csv', 'excel', 'xml'
    """
    default_image_path = path.join(
        path.dirname(path.abspath(__file__)),
        "assets",
        "astronaut.png",
    )

    file_path = default.text_blob if default else file_path
    file_path = "" if file_path is None else file_path

    match file_type:
        case "Image":
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
        case "Grayscale":
            import skimage.io

            file_path = get_file_path(file_path, default_image_path)
            return Grayscale(img=skimage.io.imread(file_path, as_gray=True))
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
