from flojoy import DataContainer, flojoy
import scipy.stats


@flojoy
def BAYES_MVS(dc, params):
    """

            Bayesian confidence intervals for the mean, var, and std.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    data : array_like
            Input data, if multi-dimensional it is flattened to 1-D by `bayes_mvs`.
            Requires 2 or more data points.
    alpha : float, optional
            Probability that the returned confidence interval contains
            the true parameter.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.bayes_mvs(
            data=dc[0].y,
            alpha=(float(params["alpha"]) if params["alpha"] != "" else None),
        ),
    )
