from flojoy import flojoy, DataContainer
from qcodes.instrument import Instrument
from typing import Optional


@flojoy(deps={"qcodes": "0.39.1"})
def CLOSE_ALL(
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The CLOSE_ALL node closes all QCoDeS instruments and should be run at the start and end of each Flojoy app that uses QCoDeS.

    Returns
    -------
    DataContainer
        optional: The input DataContainer that is returned.
    """

    Instrument.close_all()

    return default
