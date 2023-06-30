from flojoy import DataContainer, flojoy, DefaultParams
import scipy.signal

@flojoy
def STFT(default: DataContainer, default_parmas: DefaultParams, fs: float=1.0, window: str='hann', nperseg: int=256, noverlap: int=None, nfft: int=None, detrend: bool=False, return_onesided: bool=True, boundary: str='zeros', padded: bool=True, axis: int=-1, scaling: str='spectrum'):
    """
            Compute the Short Time Fourier Transform (STFT).

            STFTs can be used as a way of quantifying the change of a
            nonstationary signal's frequency and phase content over time.

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
            Length of each segment. Defaults to 256.
    noverlap : int, optional
            Number of points to overlap between segments. If `None`,
            ``noverlap = nperseg // 2``. Defaults to `None`. When
            specified, the COLA constraint must be met (see Notes below).
    nfft : int, optional
            Length of the FFT used, if a zero padded FFT is desired. If
            `None`, the FFT length is `nperseg`. Defaults to `None`.
    detrend : str or function or `False`, optional
            Specifies how to detrend each segment. If `detrend` is a
            string, it is passed as the `type` argument to the `detrend`
            function. If it is a function, it takes a segment and returns a
            detrended segment. If `detrend` is `False`, no detrending is
            done. Defaults to `False`.
    return_onesided : bool, optional
            If `True`, return a one-sided spectrum for real data. If
            `False` return a two-sided spectrum. Defaults to `True`, but for
            complex data, a two-sided spectrum is always returned.
    boundary : str or None, optional
            Specifies whether the input signal is extended at both ends, and
            how to generate the new values, in order to center the first
            windowed segment on the first input point. This has the benefit
            of enabling reconstruction of the first input point when the
            employed window function starts at zero. Valid options are
            ``['even', 'odd', 'constant', 'zeros', None]``. Defaults to
            'zeros', for zero padding extension. I.e. ``[1, 2, 3, 4]`` is
            extended to ``[0, 1, 2, 3, 4, 0]`` for ``nperseg=3``.
    padded : bool, optional
            Specifies whether the input signal is zero-padded at the end to
            make the signal fit exactly into an integer number of window
            segments, so that all of the signal is included in the output.
            Defaults to `True`. Padding occurs after boundary extension, if
            `boundary` is not `None`, and `padded` is `True`, as is the
            default.
    axis : int, optional
            Axis along which the STFT is computed; the default is over the
            last axis (i.e. ``axis=-1``).
    scaling: {'spectrum', 'psd'}
            The default 'spectrum' scaling allows each frequency line of `Zxx` to
            be interpreted as a magnitude spectrum. The 'psd' option scales each
            line to a power spectral density - it allows to calculate the signal's
            energy by numerically integrating over ``abs(Zxx)**2``.

    .. versionadded:: 1.9.0
    """
    return DataContainer(x=dc[0].y, y=scipy.signal.stft(x=dc[0].y, fs=float(params['fs']) if params['fs'] != '' else None, window=str(params['window']) if params['window'] != '' else None, nperseg=int(params['nperseg']) if params['nperseg'] != '' else None, noverlap=int(params['noverlap']) if params['noverlap'] != '' else None, nfft=int(params['nfft']) if params['nfft'] != '' else None, detrend=bool(params['detrend']) if params['detrend'] != '' else None, return_onesided=bool(params['return_onesided']) if params['return_onesided'] != '' else None, boundary=str(params['boundary']) if params['boundary'] != '' else None, padded=bool(params['padded']) if params['padded'] != '' else None, axis=int(params['axis']) if params['axis'] != '' else None, scaling=str(params['scaling']) if params['scaling'] != '' else None))