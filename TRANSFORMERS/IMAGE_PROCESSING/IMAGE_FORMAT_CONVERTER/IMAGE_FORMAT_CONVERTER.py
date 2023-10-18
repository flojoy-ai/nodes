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
        The formatted Numpy array of the image
    """
    if isinstance(default, Grayscale):
        img = default.m [np.newaxis,...]
    else:
        if default.a is None:
            img = np.stack(
                (
                    default.r[np.newaxis,...], 
                    default.g[np.newaxis,...], 
                    default.b[np.newaxis,...]
                ), axis=1
            )
        else:
            img = np.stack(
                (
                    default.r[np.newaxis,...], 
                    default.g[np.newaxis,...], 
                    default.b[np.newaxis,...],
                    default.a[np.newaxis,...]
                ), axis=1
            )
    return Matrix(m=img)