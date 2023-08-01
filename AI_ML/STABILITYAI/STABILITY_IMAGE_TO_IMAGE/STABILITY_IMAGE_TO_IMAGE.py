from flojoy import flojoy, Image as FlojoyImage, run_in_venv
from typing import Optional
import os
from pathlib import Path
import io
import os
import warnings
import time


ACCEPTED_IMAGE_FORMATS = [".jpg", ".jpeg", ".png"]
MAX_RETRY_ATTEMPTS = 3
RETRY_SLEEP_TIME_IN_SECONDS = 1


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
@run_in_venv(
    pip_dependencies=["stability-sdk==0.8.3", "Pillow==10.0.0", "requests==2.28.1"]
)
def STABILITY_IMAGE_TO_IMAGE(
    prompt: str,
    default: Optional[FlojoyImage] = None,
    image_path: Optional[str] = None,
    width: Optional[int] = 512,
    height: Optional[int] = 512,
    cfg_scale: Optional[float] = 7.0,
) -> FlojoyImage:
    """
    This node uses Stability AI Image-to-Image API to generate an image based on an input image and a text prompt.
    The image can be provided as a image file path or as a DataContainer Image object from a previous node.
    The previous node value has priority over the file path.

    Parameters:
    - image_path: string
        Path to the image file to be transcribed. []".jpg", ".jpeg", ".png"] format are supported.
    - prompt: string
        Text prompt to be used for image generation.
    - width: int
        Width of the generated image.
    - height: int
        Height of the generated image.
    - cfg_scale: float
        Influences how strongly your generation is guided to match your prompt,
        higher values means more influence. Defaults to 7.0 if not specified.
    """
    import numpy as np
    from PIL import Image
    from stability_sdk import client
    import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

    model = "stable-diffusion-v1-5"
    api_key = os.environ.get("STABILITY_API_KEY")
    if not api_key:
        raise ValueError("STABILITY_API_KEY environment variable is required")
    stability_api = client.StabilityInference(key=api_key, verbose=True, engine=model)

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

    for _ in range(MAX_RETRY_ATTEMPTS):
        try:
            answers = stability_api.generate(
                prompt=prompt,
                init_image=img,
                width=width,
                height=height,
                cfg_scale=cfg_scale,
            )

            output_image = get_image_from_answers(answers)
            break
        except Exception as e:
            print(f"Error while generating image: {e}")
            time.sleep(RETRY_SLEEP_TIME_IN_SECONDS)

    if not output_image:
        raise Exception("Something went wrong when generating image.")

    img_array = np.asarray(output_image)
    red_channel = img_array[:, :, 0]
    green_channel = img_array[:, :, 1]
    blue_channel = img_array[:, :, 2]

    alpha_channel = None
    if img_array.shape[2] == 4:
        alpha_channel = img_array[:, :, 3]

    return FlojoyImage(r=red_channel, g=green_channel, b=blue_channel, a=alpha_channel)
