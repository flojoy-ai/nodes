import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def PCG64DXSM(dc: list, params: dict) -> DataContainer:
    """
    numpy.random.PCG64DXSM
    ------------------------
    PCG64DXSM is a 64-bit variant of the PCG family of random number generators
    using the XSH RS scheme.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    seed : {None, int, array_like[ints], SeedSequence}, optional
        A seed to initialize the `BitGenerator`. If None, then fresh,
        unpredictable entropy will be pulled from the OS. If an ``int`` or
        ``array_like[ints]`` is passed, then it will be passed to
        `SeedSequence` to derive the initial `BitGenerator` state. One may also
        pass in a `SeedSequence` instance.

    Notes
    -----
    PCG-64 DXSM is a 128-bit implementation of O'Neill's permutation congruential
    generator ([1]_, [2]_). PCG-64 DXSM has a period of :math:`2^{128}` and supports
    advancing an arbitrary number of steps as well as :math:`2^{127}` streams.
    The specific member of the PCG family that we use is PCG CM DXSM 128/64. It
    differs from ``PCG64`` in that it uses the stronger DXSM output function,
    a 64-bit "cheap multiplier" in the LCG, and outputs from the state before
    advancing it rather than advance-then-output.

    ``PCG64DXSM`` provides a capsule containing function pointers that produce
    doubles, and unsigned 32 and 64- bit integers. These are not
    directly consumable in Python and must be consumed by a ``Generator``
    or similar object that supports low-level access.

    Supports the method :meth:`advance` to advance the RNG an arbitrary number of
    steps. The state of the PCG-64 DXSM RNG is represented by 2 128-bit unsigned
    integers.

    **State and Seeding**

    The ``PCG64DXSM`` state vector consists of 2 unsigned 128-bit values,
    which are represented externally as Python ints. One is the state of the
    PRNG, which is advanced by a linear congruential generator (LCG). The
    second is a fixed odd increment used in the LCG.

    The input seed is processed by `SeedSequence` to generate both values. The
    increment is not independently settable.

    **Parallel Features**

    The preferred way to use a BitGenerator in parallel applications is to use
    the `SeedSequence.spawn` method to obtain entropy values, and to use these
    to generate new BitGenerators:

    >>> from numpy.random import Generator, PCG64DXSM, SeedSequence
    >>> sg = SeedSequence(1234)
    >>> rg = [Generator(PCG64DXSM(s)) for s in sg.spawn(10)]

    **Compatibility Guarantee**

    ``PCG64DXSM`` makes a guarantee that a fixed seed will always produce
    the same random integer stream.

    References
    ----------
    .. [1] `"PCG, A Family of Better Random Number Generators"
            <http://www.pcg-random.org/>`_
    .. [2] O'Neill, Melissa E. `"PCG: A Family of Simple Fast Space-Efficient
            Statistically Good Algorithms for Random Number Generation"
            <https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf>`_

    """
    # Strictly type all internal variables
    a: int = params.get("a", 0)
    b: int = params.get("b", 0)
    c: int = params.get("c", 0)

    # Return the DataContainer instance
    return DataContainer(x=dc[0].y, y=np.random.PCG64DXSM(a=int(a), b=int(b), c=int(c)))
