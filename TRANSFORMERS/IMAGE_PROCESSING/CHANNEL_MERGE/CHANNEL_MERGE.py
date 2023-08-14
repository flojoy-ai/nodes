from flojoy import flojoy, Image

@flojoy
def CHANNEL_MERGE(
    red: Image, 
    blue: Image, 
    green: Image, 
    alpha: Image
) -> Image:
    """
    The CHANNEL_MERGE node returns the merged rgba channels of an image 

    Returns
    -------
    Image
        The image with each channel given by the appropriate channel 
        on the respective inputs
    """

    try:

        return Image(
            r=red.r,
            b=blue.b,
            g=green.g,
            a=alpha.a
        )
    except Exception as e:
        raise e
