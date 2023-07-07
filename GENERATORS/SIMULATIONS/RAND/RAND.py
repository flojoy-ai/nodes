import random
import numpy as np
from flojoy import flojoy, OrderedPair, Scalar
from typing import Literal, Optional


@flojoy
def RAND(
    default: Optional[OrderedPair] = None, distribution: Literal["normal", "uniform", "poisson"] = "normal"
) -> OrderedPair | Scalar:
    """The RAND node generates a random number or a list of random numbers
    depending on the distribution selected.

    Parameters
    ----------
    distribution : select
        the distribution over the random samples

    Returns:
    -------
    DataContainer:
        type 'ordered pair'
    """

    seed: int = random.randint(1, 10000)
    my_generator = np.random.default_rng(seed)
    if default is not None:
        x = default.x
        y = getattr(my_generator, distribution)(size=len(x))
        return OrderedPair(x=x, y=y)
    else:
        y = getattr(my_generator, distribution)(size=1)
        return Scalar(c=y)


@flojoy
def RAND_MOCK(default: Optional[OrderedPair] = None) -> OrderedPair:
    x = None
    if default is not None:
        x = default.y
        y = x
    else:
        y = np.full(
            1000, 1000
        )  # for reproducibility returning an array with constant values
    return OrderedPair(x=x, y=y)
