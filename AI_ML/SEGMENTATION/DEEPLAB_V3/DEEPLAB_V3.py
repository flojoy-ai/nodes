from flojoy import flojoy, DataContainer
import torch
from torchvision import transforms
import torchvision.transforms.functional as TF
from PIL import Image
import numpy as np


@flojoy
def DEEPLAB_V3(
    default: DataContainer,
) -> DataContainer:
    """The DEEPLAB_V3 node returns a segmentation mask from an input image
    in a dataframe. The input image is expected to be a DataContainer of type
    "image". The output is a DataContainer of type "image" with the same
    dimensions as the input image, but with the red, green, and blue channels
    replaced with the segmentation mask.

    Parameters
    ----------
    None

    Returns:
    --------
    DataContainer:
        A DataContainer with the following fields:
            type: "image"
            r: The red channel of the image
            g: The green channel of the image
            b: The blue channel of the image
            a: The alpha channel of the image

    """
    if len(dc_inputs) != 1 or dc_inputs[0].type != "image":
        raise ValueError(
            f"Invalid input, expected exactly one DataContainer of type 'image'"
        )
    input_image = dc_inputs[0]
    (r, g, b, a) = (input_image.r, input_image.g, input_image.b, input_image.a)
    nparray = (
        np.stack((r, g, b, a), axis=2) if a is not None else np.stack((r, g, b), axis=2)
    )
    input_image = TF.to_pil_image(nparray).convert("RGB")
    model = torch.hub.load(
        "pytorch/vision:v0.10.0", "deeplabv3_resnet50", pretrained=True
    )
    model.eval()
    preprocess_transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    input_tensor = preprocess_transform(input_image)
    input_batch = input_tensor.unsqueeze(0)
    with torch.no_grad():
        output = model(input_batch)["out"][0]
    output_predictions = output.argmax(0)
    palette = torch.tensor([2**25 - 1, 2**15 - 1, 2**21 - 1])
    colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
    colors = (colors % 255).numpy().astype("uint8")
    r = Image.fromarray(output_predictions.byte().cpu().numpy()).resize(
        input_image.size
    )
    r.putpalette(colors)
    out_img = np.array(r.convert("RGB"))
    return DataContainer(
        type="image", r=out_img[:, :, 0], g=out_img[:, :, 1], b=out_img[:, :, 2], a=None
    )
