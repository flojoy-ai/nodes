from flojoy import flojoy, DataContainer
from typing import List
import openai
import pandas as pd
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import io
import os
import warnings
import numpy as np

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
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                output_image = Image.open(io.BytesIO(artifact.binary))
                return output_image
    return None

@flojoy
def STABILITY_IMAGE_TO_IMAGE(dc: List[DataContainer], params: dict):
    """
    This node uses StabilityAI Image-to-Image API to generate an image based on an input image and a text prompt.
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
    """


    model = "stable-diffusion-v1-5"
    stability_api = client.StabilityInference(
        key=os.environ['STABILITY_API_KEY'], # API Key reference.
        verbose=True,
        engine=model
    )

    prompt = params.get("prompt")
    width = params.get("width", 512)
    height = params.get("height", 512)


    if dc and getattr(dc[0], 'type') == 'image':
        img_array_from_dc = np.stack([dc[0].r, dc[0].g, dc[0].b], axis=2)
        img = Image.fromarray(img_array_from_dc, 'RGB')
    else:
        image_path = params.get("image_path")
        if image_path is None:
            raise ValueError("image_path parameter is missing!")
        
        img_format = Path(image_path).suffix
        if img_format not in ACCEPTED_IMAGE_FORMATS:
            raise ValueError(f"Image format {img_format} is not supported. Supported formats are {ACCEPTED_IMAGE_FORMATS}")
        
        image_path = Path(image_path)
        if not image_path.exists():
            raise ValueError(f"file {image_path} does not exist!")

        img = Image.open(image_path)

    answers = stability_api.generate(
        prompt=prompt,
        init_image=img,
        width=width, 
        height=height,
    )

    output_image = get_image_from_answers(answers)
    if not output_image:
        raise Exception("Something went wrong when generating image.")
    
    img_array = np.asarray(img)
    red_channel = img_array[:, :, 0]
    green_channel = img_array[:, :, 1]
    blue_channel = img_array[:, :, 2]

    alpha_channel = None
    if img_array.shape[2] == 4:
        alpha_channel = img_array[:, :, 3]

    return DataContainer(
        type="image",
        r=red_channel,
        g=green_channel,
        b=blue_channel,
        a=alpha_channel
    )
