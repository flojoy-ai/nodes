import random
import numpy as np
from flojoy import flojoy, DataContainer
import traceback


@flojoy
def RAND(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """ The RAND node generates a random number or a list of numbers with
    various different distributions
    Parameters
    ----------
    size: The number of random numbers
    distribution: the distribution over the random samples

    Returns:
    -------
    scalar
        c: The list of random numbers

    """
    size: int = params["size"]
    distribution: str = params["distribtuion"]
    seed: int = random.randint(-10000, 10000)
    my_generator = np.random.default_rng(seed)
    if len(dc_inputs) > 0:
        x = dc_inputs[0].y
        y = getattr(my_generator, distribution)(size=len(x))
    else:
        y = getattr(my_generator, distribution)(size=size)

    return DataContainer(type='scalar', c=y)


# @flojoy
# def RAND_MOCK(dc_inputs, params):
#     print("running mock version of rand")
#     x = None
#     if len(dc_inputs) > 0:
#         x = dc_inputs[0].y
#         y = x
#     else:
#         y = np.full(
#             1000, 1000
#         )  # for reproducibility returning an array with constant values
#     return DataContainer(x=x, y=y)
