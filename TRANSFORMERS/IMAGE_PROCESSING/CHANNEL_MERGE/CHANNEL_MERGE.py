from flojoy import flojoy, Image, Plotly

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
    CHANNEL_OUTPUTS
        The images, each channel itself is rendered with alpha=1, except
        the alpha channel itself.
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
