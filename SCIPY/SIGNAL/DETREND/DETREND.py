from flojoy import DataContainer, flojoy
import scipy.signal


@flojoy
def DETREND(
    default: DataContainer,
    axis: int = -1,
    type: str = "linear",
    bp: int = 0,
    overwrite_data: bool = False,
):
    """

            Remove linear trend along axis from data.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    data : array_like
            The input data.
    axis : int, optional
            The axis along which to detrend the data. By default this is the
            last axis (-1).
    type : {'linear', 'constant'}, optional
            The type of detrending. If ``type == 'linear'`` (default),
            the result of a linear least-squares fit to `data` is subtracted
            from `data`.
            If ``type == 'constant'``, only the mean of `data` is subtracted.
    bp : array_like of ints, optional
            A sequence of break points. If given, an individual linear fit is
            performed for each part of `data` between two break points.
            Break points are specified as indices into `data`. This parameter
            only has an effect when ``type == 'linear'``.
    overwrite_data : bool, optional
            If True, perform in place detrending and avoid a copy. Default is False
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.signal.detrend(
            data=dc[0].y,
            axis=int(params["axis"]) if params["axis"] != "" else None,
            type=str(params["type"]) if params["type"] != "" else None,
            bp=int(params["bp"]) if params["bp"] != "" else None,
            overwrite_data=bool(params["overwrite_data"])
            if params["overwrite_data"] != ""
            else None,
        ),
    )
