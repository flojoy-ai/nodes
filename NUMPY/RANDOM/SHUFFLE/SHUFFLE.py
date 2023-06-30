import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def SHUFFLE(dc: list, params: dict) -> DataContainer:
    """
    Shuffle the sequence x in place.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
            ----------
            x : ndarray or MutableSequence
                The array, list or mutable sequence to be shuffled.

            Returns
            -------
            None

            See Also
            --------
            random.Generator.shuffle: which should be used for new code.

            Examples
            --------
            >>> arr = np.arange(10)
            >>> np.random.shuffle(arr)
            >>> arr
            [1 7 5 2 9 4 3 6 0 8] # random

            Multi-dimensional arrays are only shuffled along the first axis:

            >>> arr = np.arange(9).reshape((3, 3))
            >>> np.random.shuffle(arr)
            >>> arr
            array([[3, 4, 5], # random
                   [6, 7, 8],
                   [0, 1, 2]])


    """
    axis = params.get("axis", -1)
    return DataContainer(x=dc[0].y, y=np.random.shuffle(dc[0].y, axis=int(axis)))
