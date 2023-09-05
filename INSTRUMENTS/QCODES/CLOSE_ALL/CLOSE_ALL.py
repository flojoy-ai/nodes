from flojoy import flojoy, DataContainer
from qcodes.instrument import Instrument
from typing import Optional


@flojoy(deps={"qcodes": "0.39.1"})
def CLOSE_ALL(
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The CLOSE_ALL node closes all qcodes instruments and should be ran at
    the end of each Flojoy app that uses qcodes (and possibly the beginning).

    Returns
    -------
    DataContainer
        optional: The input DataContainer is returned.
    """

    Instrument.close_all()

    return default
