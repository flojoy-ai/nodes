from flojoy import flojoy, Image, Grayscale
import cv2
import numpy as np
from typing import Literal
from enum import Enum

class options(Enum):
    cubic = cv2.INTER_CUBIC,
    nearest = cv2.INTER_NEAREST,
    linear = cv2.INTER_LINEAR
    area = cv2.INTER_AREA
    Lanczos = cv2.INTER_LANCZOS4

@flojoy(deps={"opencv-python": "4.8.0.76"})
def IMAGE_RESIZE(
    default: Image | Grayscale,
    fx: float = 2,
    fy: float = 2,
    interpolation: Literal["nearest", "linear", "cubic", "area", "Lanczos"] = "linear",
) -> Image | Grayscale:
    """The IMAGE_RESIZE nodes provides image rescaling on either an Image or Grayscale object. 
    The method of rescaling can be adjusted, as well as the degree of scaling in each direction. 
    There are a few methods by which one can scale an image:

    - nearest       :       a nearest-neighbor interpolatino
    - linear        :       a bilinear interpolation (default)
    - area          :       resampling using pixel area relation. For 
                            decimation, this is preferred to give Moiré 
                            free results, but when zooming it is similar to the nearest method
    - cubic         :       a bicubic interoplation over 4x4 neighborhood
    - Lanczos       :       a Lanczos interpolation over 8x8 pixel neighborhood

    See https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#cv2.resize for details.

    Parameters
    ------
    default         :       Image or Grayscale
        The image to be resized
    fx              :       float
        Degree of scaling in the x direction (can be noninteger)
    fy              :       float
        Degree of scaling in the y direction (can be noninteger)
    interpolation   :       str
        Method of interpolation to implement

    Returns
    -------
    res             :       Image or Grayscale
        The resized image

    """
    try:
        interpolation = options[interpolation].value[0]
    except:
        interpolation = options[interpolation].value

    if isinstance(default, Image):
        if default.a is not None:
            img = cv2.merge([default.r, default.g, default.b, default.a])
        else:
            img = cv2.merge([default.r, default.g, default.b])
    elif isinstance(default, Grayscale):
        img = cv2.merge([default.m, np.zeros_like(default.m), np.zeros_like(default.m)])

    #Images should be of shapes (NX, NY, 3/4)
    res = cv2.resize(
        img, 
        dsize=(round(fx*img.shape[1]), round(fy*img.shape[0])), 
        fx = fx, 
        fy = fy, 
        interpolation=interpolation
    )
    # raise ValueError(f"{img.shape},{res.shape}")
    return Image(r=res[...,0], g=res[...,1], b=res[...,2], a=res[...,3] if default.a is not None else None) if isinstance(default, Image) else Grayscale(m=res[...,0])