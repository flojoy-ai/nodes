import random
import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from typing import Literal, Optional


@flojoy
def RAND(
    default: Optional[OrderedPair | Vector] = None,
    distribution: Literal["normal", "uniform", "poisson"] = "normal",
    lower_bound: float = 0,
    upper_bound: float = 1,
    normal_mean: float = 0,
    normal_standard_deviation: float = 1,
    poisson_events: float = 1,
) -> OrderedPair | Scalar:
    """The RAND node generates a random number or a list of random numbers
    depending on the distribution selected.

    Inputs
    ------
    default : OrderedPair|Vector
        Optional input to use as the x-axis for the random samples

    Parameters
    ----------
    distribution : select
        the distribution over the random samples
    lower_bound : float
        the lower bound of the output interval
    upper_bound : float
        the upper bound of the output interval
    normal_mean : float
        the mean or "center" of the normal distribution
    normal_standard_deviation : float
        the spread or "width" of the normal distribution
    poisson_events : float
        the expected number of events occurring in a fixed time-interval when distribution is poisson

    Returns
    -------
    OrderedPair|Scalar
        OrderedPair if there's an input
        x: the x-axis of the input
        y: the random samples

        Scalar if there is no input
        c: the random number
    """
    if upper_bound < lower_bound:
        upper_bound, lower_bound = lower_bound, upper_bound

    seed = random.randint(1, 10000)
    my_generator = np.random.default_rng(seed)

    if isinstance(default, OrderedPair):
        size = len(default.x)
        x = default.x
    elif isinstance(default, Vector):
        size = len(default.v)
        x = default.v
    else:
        size = 1

    if distribution == "uniform":
        y = my_generator.uniform(low=lower_bound, high=upper_bound, size=size)
    elif distribution == "normal":
        y = my_generator.normal(
            loc=normal_mean, scale=normal_standard_deviation, size=size
        )
    elif "poisson":
        y = my_generator.poisson(lam=poisson_events, size=size)

    return OrderedPair(x=x, y=y) if default else Scalar(c=y)
