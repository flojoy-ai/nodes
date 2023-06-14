from flojoy import flojoy, DataContainer
from flojoy.hflib.hub_models import HubModelFactory, ImageCaptionModels

import torchvision.transforms.functional as TF
import numpy as np
import pandas as pd


@flojoy
def NLP_CONNECT_VIT_GPT2(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The NLP_CONNECT_VIT_GPT2 node captions an input image and produces an output string wrapped
    in a dataframe.

    Parameters
    ----------

    Returns:
    --------
    DataContainer:
        type 'dataframe' containing the caption column, and a single row.

    """

    if len(dc_inputs) != 1 or dc_inputs[0].type != "image":
        raise ValueError(
            f"Invalid input, expected exactly one DataContainer of type 'image'"
        )

    input_image = dc_inputs[0]

    r, g, b, a = input_image.r, input_image.g, input_image.b, input_image.a
    nparray = (
        np.stack((r, g, b, a), axis=2) if a is not None else np.stack((r, g, b), axis=2)
    )
    image = TF.to_pil_image(nparray).convert("RGB")

    hub_model = HubModelFactory.create_model(ImageCaptionModels.NLP_CONNECT_VIT_GPT2)
    hub_model.download_and_cache()
    model, feature_extractor, tokenizer = hub_model.get_executable_model()
    pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
    output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    pred = preds[0].strip()

    df_pred = pd.DataFrame.from_records([(pred,)], columns=["caption"])

    return DataContainer(type="dataframe", m=df_pred)
