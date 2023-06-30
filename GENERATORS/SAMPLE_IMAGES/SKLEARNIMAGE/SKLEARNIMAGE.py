from typing import Literal
from flojoy import flojoy, DataContainer, DefaultParams
from skimage import data

@flojoy
def SKLEARNIMAGE(default: DataContainer, default_parmas: DefaultParams, img_key: Literal['astronaut', 'binary_blobs', 'brain', 'brick', 'camera', 'cat', 'cell', 'cells3d', 'checkerboard', 'chelsea', 'clock', 'coffee', 'coins', 'colorwheel', 'create_image_fetcher', 'data_dir', 'download_all', 'eagle', 'file_hash', 'grass', 'gravel', 'horse', 'hubble_deep_field', 'human_mitosis', 'image_fetcher', 'immunohistochemistry', 'kidney', 'lbp_frontal_face_cascade_filename', 'lfw_subset', 'lily', 'logo', 'microaneurysms', 'moon', 'nickel_solidification', 'page', 'protein_transport', 'retina', 'rocket', 'shepp_logan_phantom', 'skin', 'stereo_motorcycle', 'text', 'vortex']='astronaut') -> DataContainer:
    """Node designed to load example images from scikit-image.

    Examples can be found here:
    https://scikit-image.org/docs/stable/auto_examples/index.html

    """
    img_array = getattr(data, img_key)()
    if len(img_array.shape) == 2:
        red = green = blue = img_array
        alpha = None
    elif len(img_array.shape) == 3:
        if img_array.shape[2] == 3:
            (red, green, blue) = (img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2])
            alpha = None
        elif img_array.shape[2] == 4:
            (red, green, blue, alpha) = (img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2], img_array[:, :, 3])
    return DataContainer(type='image', r=red, g=green, b=blue, a=alpha)