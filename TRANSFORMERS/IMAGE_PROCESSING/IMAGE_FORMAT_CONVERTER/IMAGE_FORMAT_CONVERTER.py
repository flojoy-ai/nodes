from flojoy import flojoy, Image, Grayscale, Matrix
import numpy as np

@flojoy
def IMAGE_FORMAT_CONVERTER(
    default: Image | Grayscale,
) -> Matrix:
    """
    This node converts images from Flojoy's builtin Image or Grayscale format into a Numpy array of the following shape:

    # Channels x Height x Width

    for use in postprocessing.

    Parameters
    ----------
    default     :       Image or Grayscale
        The image whose format is to be converted
    
    Returns
    -------
    retval      :       Matrix  
        The formatted Numpy array of the image, in shape #Channels x H x W
    """
    if isinstance(default, Grayscale):
        img = default.m[np.newaxis,...]
    else:
        if default.a is None:
            img = np.vstack(
                (
                    default.r, 
                    default.g, 
                    default.b
                )
            )
        else:
            img = np.vstack(
                (
                    default.r, 
                    default.g, 
                    default.b,
                    default.a
                )
            )
    return Matrix(m=img)