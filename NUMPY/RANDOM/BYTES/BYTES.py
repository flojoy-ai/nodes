import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def BYTES(dc: list, params: dict) -> DataContainer:
    """
    Return random bytes.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    length : int
        Number of random bytes.

    Returns
    -----------
    seed : {None, int, array_like[ints], SeedSequence}, optional
        A seed to initialize the `BitGenerator`. If None, then fresh,
        unpredictable entropy will be pulled from the OS. If an ``int`` or
        ``array_like[ints]`` is passed, then it will be passed to
        ~`numpy.random.SeedSequence` to derive the initial `BitGenerator` state.
        One may also pass in a `SeedSequence` instance.

    Attributes
    ----------
    lock : threading.Lock
        Lock instance that is shared so that the same BitGenerator can
        be used in multiple Generators without corrupting the state. Code that
        generates values from a bit generator should hold the bit generator's
        lock.

    See Also
    --------
    SeedSequence
    out : bytes
        String of length `length`.

    See Also
    --------
    random.Generator.bytes: which should be used for new code.

    Examples
    --------
    >>> np.random.bytes(10)
    b' eh\x85\x022SZ\xbf\xa4' #random

    """
    length: int = params.get("length", 1)
    return DataContainer(x=dc[0].y, y=np.random.bytes(int(length)))
