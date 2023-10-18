from flojoy import flojoy, Image
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
    default: Image,
    fx: int = 2,
    fy: int = 2,
    interpolation: Literal["nearest", "linear", "cubic", "area", "Lanczos"] = "cubic",
) -> Image:
    try:
        interpolation = options[interpolation].value[0]
    except:
        interpolation = options[interpolation].value
    if default.a is not None:
        img = cv2.merge([default.r, default.g, default.b, default.a])
    else:
        img = cv2.merge([default.r, default.g, default.b])
        
    #Images should be of shapes (NX, NY, 3/4)
    res = cv2.resize(
        img, 
        dsize=(round(fx*img.shape[1]), round(fy*img.shape[0])), 
        fx = fx, 
        fy = fy, 
        interpolation=interpolation
    )
    # raise ValueError(f"{img.shape},{res.shape}")
    return Image(r=res[...,0], g=res[...,1], b=res[...,2], a=res[...,3] if default.a is not None else None)