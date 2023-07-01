from flojoy import DataContainer, flojoy, DefaultParams
import scipy.signal


@flojoy
def SAVGOL_FILTER(
    default: DataContainer,
    default_params: DefaultParams,
    window_length: int = None,
    polyorder: int = None,
    deriv: int = 0,
    delta: float = 1.0,
    axis: int = -1,
    mode: str = "interp",
    cval: float = 0.0,
):
    """
            Apply a Savitzky-Golay filter to an array.

            This is a 1-D filter. If `x`  has dimension greater than 1, `axis`
            determines the axis along which the filter is applied.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            The data to be filtered. If `x` is not a single or double precision
            floating point array, it will be converted to type ``numpy.float64``
            before filtering.
    window_length : int
            The length of the filter window (i.e., the number of coefficients).
            If `mode` is 'interp', `window_length` must be less than or equal
            to the size of `x`.
    polyorder : int
            The order of the polynomial used to fit the samples.
            `polyorder` must be less than `window_length`.
    deriv : int, optional
            The order of the derivative to compute. This must be a
            nonnegative integer. The default is 0, which means to filter
            the data without differentiating.
    delta : float, optional
            The spacing of the samples to which the filter will be applied.
            This is only used if deriv > 0. Default is 1.0.
    axis : int, optional
            The axis of the array `x` along which the filter is to be applied.
            Default is -1.
    mode : str, optional
            Must be 'mirror', 'constant', 'nearest', 'wrap' or 'interp'. This
            determines the type of extension to use for the padded signal to
            which the filter is applied.  When `mode` is 'constant', the padding
            value is given by `cval`.  See the Notes for more details on 'mirror',
            'constant', 'wrap', and 'nearest'.
            When the 'interp' mode is selected (the default), no extension
            is used.  Instead, a degree `polyorder` polynomial is fit to the
            last `window_length` values of the edges, and this polynomial is
            used to evaluate the last `window_length // 2` output values.
    cval : scalar, optional
            Value to fill past the edges of the input if `mode` is 'constant'.
            Default is 0.0.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.signal.savgol_filter(
            x=dc[0].y,
            window_length=int(params["window_length"])
            if params["window_length"] != ""
            else None,
            polyorder=int(params["polyorder"]) if params["polyorder"] != "" else None,
            deriv=int(params["deriv"]) if params["deriv"] != "" else None,
            delta=float(params["delta"]) if params["delta"] != "" else None,
            axis=int(params["axis"]) if params["axis"] != "" else None,
            mode=str(params["mode"]) if params["mode"] != "" else None,
            cval=float(params["cval"]) if params["cval"] != "" else None,
        ),
    )
