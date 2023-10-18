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
    """The IMAGE_AGGREGATOR node is designed to accumulate the images that are iteratively 
    passed to it to internal memory. It has two operating modes, and is designed such that 
    an application will have two instances of this node, each operating in the respectively 
    modes.

    If the `referred_node` parameter is empty, namely that there is no place to look for 
    data, the node will operate as if it is supposed to stack images into memory. It is 
    able to do so for a stack of RGB images, and a stack of monochrome images, but not the 
    combination of the two. That would be inconsistent, and the code will complain.

    The second mode is "return" mode, where the `referred_node` will be specified to point 
    to the first instance of this node, the one that accumulated the images. In that case, 
    the node will immediately return the stack of images in the `Matrix` DataContainer 
    format.

    The stack of images are given in the following shape:
        # of images x # of channels x Height x Width

    Parameters
    ----------
    default         :       Image or Grayscale
        The next image to be added to the stack. If no stack yet exists, this
        will be used to instantiate the stack
    referred_node   :       Optional[NodeReference]
        This is the referred to node that previously stacked the images into internal memory. If this node is specified, the function will immediatelty return the stack.
    
    Return
    ------
    retval          :       Grayscale | Image | Matrix
        In aggregation mode, the node will return whatever image was just added to the stack, greyscale or not. Otherwise, the node returns the stack. 
    
    """
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
            img = np.stack(
                (
                    default.r[np.newaxis,...], 
                    default.g[np.newaxis,...], 
                    default.b[np.newaxis,...]
                ), axis=1
            )
        else:
            img = np.stack(
                (
                    default.r[np.newaxis,...], 
                    default.g[np.newaxis,...], 
                    default.b[np.newaxis,...],
                    default.a[np.newaxis,...]
                ), axis=1
            )

    data = SmallMemory().read_memory(node_id, memory_key) or {}
    
    if not data: #this means that we have not written to memory yet!
         # artificially extend the first dimension
        images = img #this now gives us something 1xCxHxW
        img_types = [str(type(default).__name__)] #should be either Image or Grayscale
    else:
        images = np.vstack(
            (
                data['images'], # this gives us something (N-1)xCxHxW
                img[np.newaxis,...] if isinstance(default, Grayscale) else img #something 1xCxHxW
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