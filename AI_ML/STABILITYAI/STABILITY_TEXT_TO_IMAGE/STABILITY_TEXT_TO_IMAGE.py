import numpy as np
from flojoy import flojoy, DataContainer
from typing import List
from PIL import Image
import requests
import os
import base64
import io



@flojoy
def STABILITY_TEXT_TO_IMAGE(dc: List[DataContainer], params: dict):
    """
    The STABILITY_TEXT_TO_IMAGE node uses the STABILITY AI Rest API to convert text to an image.
    The node returns an image.

    Parameters
    ----------
    prompt : string
        The prompt to be used to generate the image. Default is "A lighthouse on a cliff."
    width : int
        The width of the image to be generated. Default is 512.
    height : int
        The height of the image to be generated. Default is 512.
    cfg_scale: float
        Influences how strongly your generation is guided to match your prompt, 
        higher values means more influence. Defaults to 7.0 if not specified.
    """
    engine_id = "stable-diffusion-v1-5"
    api_host = "https://api.stability.ai"
    api_key = os.getenv("STABILITY_API_KEY")

    if not api_key:
        raise ValueError("STABILITY_API_KEY environment variable is required")

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    prompt = params.get("prompt")
    if prompt is None:
        raise ValueError("Prompt is required")
    prompts = [{
        "text": prompt
    }]

    img_width = params.get("width", 512)
    img_height = params.get("height", 512)
    cfg_scale = params.get("cfg_scale", 7.0)

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers=headers,
        json={
            "text_prompts": prompts,
            "height": img_width,
            "width": img_height,
            "samples": 1,
            "cfg_scale": cfg_scale
        }
    )
    data = response.json()
    image_string = data["artifacts"][0].get('base64')
    image_bytes = base64.b64decode(image_string)
    image_stream = io.BytesIO(image_bytes)
    image = Image.open(image_stream)
    del image_stream
    del image_bytes
    del image_string

    image_array = np.asarray(image)
    red_channel = image_array[:, :, 0]
    green_channel = image_array[:, :, 1]
    blue_channel = image_array[:, :, 2]

    alpha_channel = None
    if image_array.shape[2] == 4:
        alpha_channel = image_array[:, :, 3]

    return DataContainer(
        type="image",
        r=red_channel,
        g=green_channel,
        b=blue_channel,
        a=alpha_channel,
    )
