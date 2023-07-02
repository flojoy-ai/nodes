from flojoy import DataContainer, flojoy
import scipy.signal


@flojoy
def WELCH(
    default: DataContainer,
    fs: float = 1.0,
    window: str = "hann",
    nperseg: int = None,
    noverlap: int = None,
    nfft: int = None,
    detrend: str = "constant",
    return_onesided: bool = True,
    scaling: str = "density",
    axis: int = -1,
    average: str = "mean",
):
    """

            Estimate power spectral density using Welch's method.

            Welch's method [1]_ computes an estimate of the power spectral
            density by dividing the data into overlapping segments, computing a
            modified periodogram for each segment and averaging the
            periodograms.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            Time series of measurement values
    fs : float, optional
            Sampling frequency of the `x` time series. Defaults to 1.0.
    window : str or tuple or array_like, optional
            Desired window to use. If `window` is a string or tuple, it is
            passed to `get_window` to generate the window values, which are
            DFT-even by default. See `get_window` for a list of windows and
            required parameters. If `window` is array_like it will be used
            directly as the window and its length must be nperseg. Defaults
            to a Hann window.
    nperseg : int, optional
            Length of each segment. Defaults to None, but if window is str or
            tuple, is set to 256, and if window is array_like, is set to the
            length of the window.
    noverlap : int, optional
            Number of points to overlap between segments. If `None`,
            ``noverlap = nperseg // 2``. Defaults to `None`.
    nfft : int, optional
            Length of the FFT used, if a zero padded FFT is desired. If
            `None`, the FFT length is `nperseg`. Defaults to `None`.
    detrend : str or function or `False`, optional
            Specifies how to detrend each segment. If `detrend` is a
            string, it is passed as the `type` argument to the `detrend`
            function. If it is a function, it takes a segment and returns a
            detrended segment. If `detrend` is `False`, no detrending is
            done. Defaults to 'constant'.
    return_onesided : bool, optional
            If `True`, return a one-sided spectrum for real data. If
            `False` return a two-sided spectrum. Defaults to `True`, but for
            complex data, a two-sided spectrum is always returned.
    scaling : { 'density', 'spectrum' }, optional
            Selects between computing the power spectral density ('density')
            where `Pxx` has units of V**2/Hz and computing the power
            spectrum ('spectrum') where `Pxx` has units of V**2, if `x`
            is measured in V and `fs` is measured in Hz. Defaults to
            'density'
    axis : int, optional
            Axis along which the periodogram is computed; the default is
            over the last axis (i.e. ``axis=-1``).
    average : { 'mean', 'median' }, optional
            Method to use when averaging periodograms. Defaults to 'mean'.

    .. versionadded:: 1.2.0
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.signal.welch(
            x=dc[0].y,
            fs=float(params["fs"]) if params["fs"] != "" else None,
            window=str(params["window"]) if params["window"] != "" else None,
            nperseg=int(params["nperseg"]) if params["nperseg"] != "" else None,
            noverlap=int(params["noverlap"]) if params["noverlap"] != "" else None,
            nfft=int(params["nfft"]) if params["nfft"] != "" else None,
            detrend=str(params["detrend"]) if params["detrend"] != "" else None,
            return_onesided=bool(params["return_onesided"])
            if params["return_onesided"] != ""
            else None,
            scaling=str(params["scaling"]) if params["scaling"] != "" else None,
            axis=int(params["axis"]) if params["axis"] != "" else None,
            average=str(params["average"]) if params["average"] != "" else None,
        ),
    )
