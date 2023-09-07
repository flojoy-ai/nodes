from flojoy import flojoy, Image
import numpy as np


@flojoy
def CHANNEL_MERGE(red: Image, green: Image, blue: Image, alpha: Image) -> Image:
    """The CHANNEL_MERGE node returns the merged rgba channels of an image.

    Returns
    -------
    Image
        The image with each channel given by the appropriate channel
        on the respective inputs.
    """

    try:
        r = red.r
        b = blue.b
        g = green.g
        a = alpha.a

        zeros = np.zeros(r.shape, np.uint8)
        ones = 255 * np.ones(r.shape, np.uint8)

        if not (
            np.array_equal(red.g, zeros)
            and np.array_equal(red.b, zeros)
            and np.array_equal(red.a, ones)
        ):
            raise ValueError("Red input had nonzero values for the other channels.")

        if not (
            np.array_equal(blue.r, zeros)
            and np.array_equal(blue.g, zeros)
            and np.array_equal(blue.a, ones)
        ):
            raise ValueError("Blue input had nonzero values for the other channels.")

        if not (
            np.array_equal(green.r, zeros)
            and np.array_equal(green.b, zeros)
            and np.array_equal(green.a, ones)
        ):
            raise ValueError("Green input had nonzero values for the other channels.")

        if not (
            np.array_equal(alpha.r, zeros)
            and np.array_equal(alpha.b, zeros)
            and np.array_equal(alpha.b, zeros)
        ):
            raise ValueError("Alpha input had nonzero values for the other channels.")

        return Image(r=r, b=b, g=g, a=a)
    except Exception as e:
        raise e
