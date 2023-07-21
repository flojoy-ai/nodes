import numpy as np
from flojoy import flojoy, Image as FlojoyImage, run_in_venv
from typing import Optional
from PIL import Image
import os
import io
from pathlib import Path
from PIL import Image
import requests


ACCEPTED_IMAGE_FORMATS = [".jpg", ".jpeg", ".png"]
MAX_RETRY_ATTEMPTS = 3
RETRY_SLEEP_TIME_IN_SECONDS = 1


@flojoy
@run_in_venv(
    pip_dependencies=[
        "Pillow==10.0.0",
        "requests==2.28.1"
    ]
)
def STABILITY_UPSCALING(
    default: Optional[FlojoyImage] = None,
    image_path: Optional[str] = None,
    output_width: int = 1024,
) -> FlojoyImage:
    """
    The STABILITY_UPSCALING node uses the STABILITY AI gRCP API to upscale an image.
    The image can be passed as input to the node using form data or by a previous node in the flow.

    Parameters
    ----------
    image_path: Optional[string]
        The path to the image to be upscaled.
    output_width : int
        The output image width. Default is 1024.
    """
    engine_id = "esrgan-v1-x2plus"
    api_key = os.getenv("STABILITY_API_KEY")
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')

    if not api_key:
        raise ValueError("STABILITY_API_KEY environment variable is required")

    if default and getattr(default, "type") == "image":
        img_array_from_dc = np.stack([default.r, default.g, default.b], axis=2)
        img = Image.fromarray(img_array_from_dc, "RGB")
    else:
        if image_path is None:
            raise ValueError("image_path parameter is missing!")

        img_format = Path(image_path).suffix
        if img_format not in ACCEPTED_IMAGE_FORMATS:
            raise ValueError(
                f"Image format {img_format} is not supported. Supported formats are {ACCEPTED_IMAGE_FORMATS}"
            )

        image_path = Path(image_path)
        if not image_path.exists():
            raise ValueError(f"file {image_path} does not exist!")

        img = Image.open(image_path)

    
    byte_io = io.BytesIO()
    img.save(byte_io, 'png')
    byte_io.seek(0)

    for _ in range(MAX_RETRY_ATTEMPTS):
        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/image-to-image/upscale",
            headers={
                "Accept": "image/png",
                "Authorization": f"Bearer {api_key}"
            },
            files={
                "image": byte_io
            },
            data={
                "width": output_width,
            }
        )
        if response.status_code != 500:
            break

    if response.status_code != 200:
        print('Request failed with status code:', response.status_code)

    output_image = Image.open(io.BytesIO(response.content))
    img_array = np.asarray(output_image)
    red_channel = img_array[:, :, 0]
    green_channel = img_array[:, :, 1]
    blue_channel = img_array[:, :, 2]

    alpha_channel = None
    if img_array.shape[2] == 4:
        alpha_channel = img_array[:, :, 3]

    return FlojoyImage(
        r=red_channel, 
        g=green_channel, 
        b=blue_channel,
        a=alpha_channel
    )
