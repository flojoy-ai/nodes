from flojoy import flojoy, DataContainer
from skimage import data


@flojoy
def SKLEARNIMAGE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node designed to load example images from scikit-image.

    Examples can be found here:
    https://scikit-image.org/docs/stable/auto_examples/index.html

    """
    img_key = params["img_key"]

    img_array = getattr(data, img_key)()

    if len(img_array.shape) == 2:
        red = green = blue = img_array
        alpha = None
    elif len(img_array.shape) == 3:
        # Color image
        if img_array.shape[2] == 3:
            red, green, blue = (
                img_array[:, :, 0],
                img_array[:, :, 1],
                img_array[:, :, 2],
            )
            alpha = None
        elif img_array.shape[2] == 4:
            red, green, blue, alpha = (
                img_array[:, :, 0],
                img_array[:, :, 1],
                img_array[:, :, 2],
                img_array[:, :, 3],
            )

    return DataContainer(
        type="image",
        r=red,
        g=green,
        b=blue,
        a=alpha,
    )
