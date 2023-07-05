import numpy as np
from flojoy import flojoy, DataContainer
from typing import List
import openai
from PIL import Image
import requests
from io import BytesIO
import os


@flojoy
def DALLE_IMAGE_GENERATOR(dc: List[DataContainer], params):
    """
    The DALLE_IMAGE_GENERATOR node takes a prompt and generates an image 
    using OpenAI's DALL-E model.
    The prompt should be a sentence describing the image you want to generate.
    The image will be returned as a DataContainer with the type 'image'.

    Parameters:
    - prompt: string
        A sentence describing the image you want to generate.
    """
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    prompt = params.get('prompt')
    result = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    if not result.data:
        raise Exception('No image data in result')

    url = result.data[0].get('url')
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

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
        a=alpha_channel,
    )
