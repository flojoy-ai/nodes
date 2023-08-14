from flojoy import flojoy, Image
from typing import TypedDict
import numpy as np

class CHANNEL_OUTPUTS(TypedDict):
    r: Image
    g: Image
    b: Image 
    a: Image


@flojoy
def CHANNEL_SPLIT(default: Image) -> CHANNEL_OUTPUTS:
    """
    The CHANNEL_SPLIT node returns the rgba channels of an image 
    into 4 separate images for direct visualization

    Returns
    -------
    CHANNEL_OUTPUTS
        The images, each channel itself is rendered with alpha=1, except
        the alpha channel itself.
    """

    r = default.r
    g = default.g
    b = default.b
    a = default.a
    
    try:

        zeros = np.zeros(b.shape, np.uint8)
        ones = 255*np.ones(b.shape, np.uint8)

        return CHANNEL_OUTPUTS(
            r=Image(
                r=r,
                g=zeros,
                b=zeros,
                a=ones,
            ), 
            g=Image(
                r=zeros,
                g=g,
                b=zeros,
                a=ones,
            ), 
            b=Image(
                r=zeros,
                g=zeros,
                b=b,
                a=ones,
            ), 
            a=Image(
                r=zeros,
                g=zeros,
                b=zeros,
                a=a,
            ), 
        )
    except Exception as e:
        raise e
