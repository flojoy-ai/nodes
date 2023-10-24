from scipy.signal import find_peaks, peak_widths
from flojoy import flojoy, OrderedPair
from typing import TypedDict


class resultSplit(TypedDict):
    heights: OrderedPair
    widths: OrderedPair


@flojoy
def PEAK_DETECTION(
    default: OrderedPair,
    height: float = None,
    threshold: float = None,
    distance: float = None,
    prominence: float = None,
    width: float = None,
    wlen: float = None,
    rel_height: float = None,
    plateau_size: float = None,
) -> resultSplit:
    """The PEAK_DETECTION node finds peaks based on peak properties.

    The first output returns the peaks heights and the second returns the
    peak widths.

    Many of the parameters are based in Samples (number of points) rather than
    in the x axis scale.

    Inputs
    ------
    default : OrderedPair
        The data to find peaks in.

    Parameters
    ----------
    height : float, optional
        Required height of peaks. Either a number or `None`.
    threshold : float, optional
        Required threshold of peaks, the vertical distance to its neighboring
        samples. Either a number or `None`
    distance : float, optional
        Required minimal horizontal distance (>= 1) in samples between
        neighbouring peaks. Smaller peaks are removed first until the condition
        is fulfilled for all remaining peaks.
    prominence : float, optional
        Required prominence of peaks. Either a number or `None`
    width : float, optional
        Required width of peaks in samples. Either a number or `None`
    wlen : int, optional
        Used for calculation of the peaks prominences, thus it is only used if
        one of the arguments `prominence` or `width` is given. See argument
        `wlen` in `peak_prominences` for a full description of its effects.
    rel_height : float, optional
        Used for calculation of the peaks width, thus it is only used if `width`
        is given. See scipy.signal.peak_widths at docs.scipy.org.
    plateau_size : float, optional
        Required size of the flat top of peaks in samples. Either a number
        or `None`

    Returns
    -------
    heights : OrderedPair
        x: x axis location for peaks
        y: peak heights
    widths : OrderedPair
        x: x axis location for peaks
        y: peak widths
    """

    signal = default.y
    freq = default.x

    peaks, _ = find_peaks(
        signal,
        height=height,
        threshold=threshold,
        distance=distance,
        prominence=prominence,
        width=width,
        wlen=wlen,
        rel_height=rel_height,
        plateau_size=plateau_size,
    )

    widths = peak_widths(signal, peaks)
    widths = widths[0] * freq.max() / freq.shape[0]  # Samples to x axis scale.

    properties = resultSplit(
        heights=OrderedPair(x=freq[peaks], y=signal[peaks]),
        widths=OrderedPair(x=freq[peaks], y=widths),
    )

    return properties
