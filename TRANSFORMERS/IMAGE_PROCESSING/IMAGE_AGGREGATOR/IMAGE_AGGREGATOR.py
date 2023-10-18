from flojoy import flojoy, Image, Grayscale, SmallMemory, DefaultParams, Matrix, NodeReference
from typing import Any, Optional
import numpy as np

memory_key = "IMAGE_AGGREGATOR"

@flojoy(inject_node_metadata=True)
def IMAGE_AGGREGATOR(
    default: Image | Grayscale,
    default_params: DefaultParams,
    referred_node: Optional[NodeReference] = None
) -> Image | Grayscale | Matrix:
    data: dict[str, Any]
    if referred_node.unwrap() != "":
        data = SmallMemory().read_memory(referred_node.unwrap(), memory_key)
        return Matrix(m=data['images'])
    

    node_id = default_params.node_id
    # Our final result will be NxCxHxW 
    if isinstance(default, Grayscale):
        img = default.m  
    else:
        if default.a is None:
            img = np.vstack((default.r, default.g, default.b))
        else:
            img = np.vstack((default.r, default.g, default.b, default.a))

    data = SmallMemory().read_memory(node_id, memory_key) or {}
    
    if not data: #this means that we have not written to memory yet!
         # artificially extend the first dimension
        images = img[np.newaxis,...] #this now gives us something 1xCxHxW
        img_types = [str(type(default).__name__)] #should be either Image or Grayscale
    else:
        images = np.vstack(
            (
                data['images'], # this gives us something (N-1)xCxHxW
                img[np.newaxis,...] #something 1xCxHxW
                ), 
        )
        img_types = data['img_types'] + [str(type(default).__name__)]
        if not all(x == img_types[0] for x in img_types):
            raise TypeError("Attempting to stack RGB (monochrome) image onto chain of monochrome (RGB) images.")
    SmallMemory().write_to_memory(
        node_id,
        memory_key,
        {
            "node_id": node_id,
            "images" : images,
            "img_types" : img_types
        },
    )

    #pass the image processed as a result for viz or whatnot
    return default