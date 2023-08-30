from flojoy import flojoy, DataContainer, Scalar
from qcodes.instrument import Instrument
from typing import Optional


@flojoy(deps={"qcodes": "0.39.1"})
def CLOSE_ALL(
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The CLOSE_ALL node closes all qcodes instruments and should be ran at
    the beginning and end of each Flojoy app that uses qcodes.

    Returns
    -------
    Scalar
        c: placeholder for testing purposes.
    """

    Instrument.close_all()

    match default:
        case None:
            return Scalar(c=0.0)
        case _:
            return default
