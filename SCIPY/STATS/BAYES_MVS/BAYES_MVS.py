from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type="default")
def BAYES_MVS(
    default: OrderedPair,
    alpha: float = 0.9,
) -> OrderedPair:
    """The BAYES_MVS node is based on a numpy or scipy function.
    The description of that function is as follows:


            Bayesian confidence intervals for the mean, var, and std.

    Parameters
    ----------
    data : array_like
            Input data, if multi-dimensional it is flattened to 1-D by `bayes_mvs`.
            Requires 2 or more data points.
    alpha : float, optional
            Probability that the returned confidence interval contains
            the true parameter.

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=scipy.stats.bayes_mvs(
            data=default.y,
            alpha=alpha,
        ),
    )
    return result
