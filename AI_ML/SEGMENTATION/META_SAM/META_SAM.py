from flojoy import flojoy, DataContainer
import node_venv



@flojoy
@node_venv.run_in_venv(
    pip_dependencies=[
        "torch==1.11.0",
        "torchvision==0.12.0",
        "opencv-python-headless",
        "pycocotools",
        "matplotlib",
        "onnxruntime",
        "onnx",
        "pillow",
        "huggingface_hub",
        "git+https://github.com/facebookresearch/segment-anything.git"
])
def META_SAM(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The META_SAM node runs the SegmentAnythingModel (SAM) on an image.

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

    import cv2
    import numpy as np
    from PIL import Image

    from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
    from huggingface_hub import hf_hub_download

    if len(dc_inputs) != 1 or dc_inputs[0].type != "image":
        raise ValueError(
            f"Invalid input, expected exactly one DataContainer of type 'image'"
        )
    

    input_image = dc_inputs[0]

    r, g, b, a = input_image.r, input_image.g, input_image.b, input_image.a
    nparray = (
        np.stack((r, g, b, a), axis=2) if a is not None else np.stack((r, g, b), axis=2)
    )

    img_format = "RGBA"
    img_rgba = np.array(Image.fromarray(nparray).convert(img_format))

    chkpt_path = hf_hub_download("ybelkada/segment-anything", "checkpoints/sam_vit_b_01ec64.pth")
    sam = sam_model_registry["vit_b"](checkpoint=chkpt_path)
    mask_generator = SamAutomaticMaskGenerator(sam)
    masks = mask_generator.generate(nparray)

    def _get_overlay(anns):
        if len(anns) == 0:
            return None
        sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
        img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
        img[:,:,3] = 0
        for ann in sorted_anns:
            m = ann['segmentation']
            color_mask = np.concatenate([np.random.random(3), [0.35]])
            img[m] = color_mask
        return (img * 255).astype(np.uint8)

    overlay = _get_overlay(masks)
    # Overlay the overlay on top of img_rgba, using cv2
    if overlay is not None:
        img_rgba = cv2.addWeighted(img_rgba, 1, overlay, 0.5, 0)

    return DataContainer(
        type="image",
        r=img_rgba[:, :, 0],
        g=img_rgba[:, :, 1],
        b=img_rgba[:, :, 2],
        a=img_rgba[:, :, 3]
    )