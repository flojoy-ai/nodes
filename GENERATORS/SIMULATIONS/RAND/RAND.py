import random
import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector, display
from typing import Literal, Optional


@flojoy
def RAND(
    default: Optional[OrderedPair | Vector] = None,
    distribution: Literal["normal", "uniform", "poisson"] = "normal",
    force_scalar: bool = False,
    lower_bound: float = 0,
    upper_bound: float = 1,
    normal_mean: float = 0,
    normal_standard_deviation: float = 1,
    poisson_events: float = 1,
) -> OrderedPair | Scalar:
    """The RAND node generates a random number or a list of random numbers, depending on the distribution selected.

    Inputs
    ------
    default : OrderedPair|Vector
        Optional input to use as the x-axis for the random samples.

    Parameters
    ----------
    distribution : select
        the distribution over the random samples
    force_scalar : select
        whether to force the output to be a Scalar
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
        OrderedPair if there is an input.
        x: the x-axis of the input
        y: the random samples

        Scalar if there is no input.
        c: the random number
    """

    if upper_bound < lower_bound:
        upper_bound, lower_bound = lower_bound, upper_bound

    seed = random.randint(1, 10000)
    my_generator = np.random.default_rng(seed)

    match default:
        case OrderedPair():
            size = len(default.x)
            x = default.x
        case Vector():
            size = len(default.v)
            x = default.v
        case _:
            size = 1

    if force_scalar:
        size = 1

    match distribution:
        case "uniform":
            y = my_generator.uniform(low=lower_bound, high=upper_bound, size=size)
        case "normal":
            y = my_generator.normal(
                loc=normal_mean, scale=normal_standard_deviation, size=size
            )
        case "poisson":
            y = my_generator.poisson(lam=poisson_events, size=size)

    if not force_scalar:
        return OrderedPair(x=x, y=y) if default else Scalar(c=float(y[0]))
    elif force_scalar:
        return Scalar(c=float(y))
    else:
        raise TypeError("True/False string evaluation error.")


@display
def OVERLOAD(force_scalar, lower_bound, upper_bound, distribution="uniform") -> None:
    return None


@display
def OVERLOAD(
    force_scalar, normal_mean, normal_standard_deviation, distribution="normal"
) -> None:
    return None


@display
def OVERLOAD(poisson_events, distribution="poisson") -> None:
    return None
