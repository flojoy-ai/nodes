import numpy as np
from flojoy import flojoy, Image, run_in_venv
import openai
from PIL import Image as PilImage
import requests
from io import BytesIO
import os
import time

API_RETRY_ATTEMPTS = 5
API_RETRY_INTERVAL_IN_SECONDS = 1

@flojoy
@run_in_venv(
    pip_dependencies=[
        "openai==0.27.8",
        "Pillow==10.0.0",
        "requests==2.28.1"
    ]
)
def DALLE_IMAGE_GENERATOR(
    prompt: str,
    width: int = 1024,
    height: int = 1024,
) -> Image:
    """
    The DALLE_IMAGE_GENERATOR node takes a prompt and generates an image
    using OpenAI's DALL-E model.
    The prompt should be a sentence describing the image you want to generate.
    The image will be returned as a DataContainer with the type 'image'.

    Parameters
    ----------
    prompt: string
        A sentence describing the image you want to generate.
    width: int
        The width of the generated image.
    height: int
        The height of the generated image.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OPENAI_API_KEY environment variable not set")
    
    openai.api_key = api_key

    for i in range(API_RETRY_ATTEMPTS):
        try:
            result = openai.Image.create(prompt=prompt, n=1, size=f"{width}x{height}")
            print(f'No error in attempt {i} of generating image')
            break
        except openai.error.RateLimitError:
            if i > API_RETRY_ATTEMPTS:
                raise Exception("Rate limit error. Max retries exceeded.")

            print(f"Rate limit error, retrying in {API_RETRY_INTERVAL_IN_SECONDS} seconds")
            time.sleep(API_RETRY_INTERVAL_IN_SECONDS)
            continue

    if not result.data:
        raise Exception("No image data in result")

    url = result.data[0].get("url")
    response = requests.get(url)
    img = PilImage.open(BytesIO(response.content))

    img_array = np.asarray(img)
    red_channel = img_array[:, :, 0]
    green_channel = img_array[:, :, 1]
    blue_channel = img_array[:, :, 2]

    alpha_channel = None
    if img_array.shape[2] == 4:
        alpha_channel = img_array[:, :, 3]

    return Image(
        r=red_channel,
        g=green_channel,
        b=blue_channel,
        a=alpha_channel,
    )
