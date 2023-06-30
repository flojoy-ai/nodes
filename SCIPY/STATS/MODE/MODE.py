from flojoy import DataContainer, flojoy, DefaultParams
import scipy.stats

@flojoy
def MODE(default: DataContainer, default_parmas: DefaultParams, axis: int=0, nan_policy: str='propagate', keepdims: bool=None):
    """
            Return an array of the modal (most common) value in the passed array.

            If there is more than one such value, only one is returned.
            The bin-count for the modal bins is also returned.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : array_like
            n-dimensional array of which to find mode(s).
    axis : int or None, optional
            Axis along which to operate. Default is 0. If None, compute over
            the whole array `a`.
    nan_policy : {'propagate', 'raise', 'omit'}, optional
            Defines how to handle when input contains nan.
    The following options are available (default is 'propagate'):

    * 'propagate': treats nan as it would treat any other value
    * 'raise': throws an error
    * 'omit': performs the calculations ignoring nan values
    keepdims : bool, optional
            If set to ``False``, the `axis` over which the statistic is taken
            is consumed (eliminated from the output array) like other reduction
            functions (e.g. `skew`, `kurtosis`). If set to ``True``, the `axis` is
            retained with size one, and the result will broadcast correctly
            against the input array. The default, ``None``, is undefined legacy
            behavior retained for backward compatibility.

    .. warning::
            Unlike other reduction functions (e.g. `skew`, `kurtosis`), the
            default behavior of `mode` usually retains the the axis it acts
    along. In SciPy 1.11.0, this behavior will change: the default
            value of `keepdims` will become ``False``, the `axis` over which
            the statistic is taken will be eliminated, and the value ``None``
            will no longer be accepted.
    .. versionadded:: 1.9.0
    """
    return DataContainer(x=dc[0].y, y=scipy.stats.mode(a=dc[0].y, axis=int(params['axis']) if params['axis'] != '' else None, nan_policy=str(params['nan_policy']) if params['nan_policy'] != '' else None, keepdims=bool(params['keepdims']) if params['keepdims'] != '' else None))