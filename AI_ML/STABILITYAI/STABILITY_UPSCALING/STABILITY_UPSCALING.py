import numpy as np
from flojoy import flojoy, Image as FlojoyImage
from typing import Optional
from PIL import Image
import os
import io
from pathlib import Path
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


ACCEPTED_IMAGE_FORMATS = [".jpg", ".jpeg", ".png"]


def get_image_from_answers(answers):
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again."
                )
            if artifact.type == generation.ARTIFACT_IMAGE:
                output_image = Image.open(io.BytesIO(artifact.binary))
                return output_image
    return None


@flojoy
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

    if not api_key:
        raise ValueError("STABILITY_API_KEY environment variable is required")

    stability_api = client.StabilityInference(
        key=api_key,
        upscale_engine=engine_id,
        verbose=True,
    )

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

    answers = stability_api.upscale(
        init_image=img,
        width=int(output_width),
    )

    output_image = get_image_from_answers(answers)
    if not output_image:
        raise Exception("Something went wrong when generating image.")

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
