import random
import numpy as np
from flojoy import flojoy, DataContainer
import traceback


@flojoy
def RAND(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The RAND node generates a random number or a list of random numbers
    depending on the distribution selected.

    Parameters
    ----------
    distribution : str
        the distribution over the random samples

    Returns:
    -------
    DataContainer:
        type 'ordered pair'
    """
    distribution: str = params["distribution"]
    seed: int = random.randint(1, 10000)
    my_generator = np.random.default_rng(seed)
    if len(dc_inputs) > 0:
        x = dc_inputs[0].y
        y = getattr(my_generator, distribution)(size=len(x))
        return DataContainer(x=x, y=y)
    else:
        y = getattr(my_generator, distribution)(size=1)
        return DataContainer(type="scalar", c=y)


@flojoy
def RAND_MOCK(dc_inputs, params):
    print("running mock version of rand")
    x = None
    if len(dc_inputs) > 0:
        x = dc_inputs[0].y
        y = x
    else:
        y = np.full(
            1000, 1000
        )  # for reproducibility returning an array with constant values
    return DataContainer(x=x, y=y)
