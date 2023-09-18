from flojoy import flojoy, DataContainer, TextBlob
import pyvisa
from typing import Optional


@flojoy(
    deps={
        "pyvisa": "1.13.0",
        "pyusb": "1.2.1",
        "zeroconf": "0.102.0",
        "pyvisa_py": "0.7.0",
    }
)
def VISA_IDENTITY(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The VISA_IDENTITY node send an identity query ("*IDN?") to the specified instrument.

    If the "VISA_address" parameter is not specified the VISA_index will be
    used to find the address. The LIST_VISA node can be used to show the
    indicies of all available VISA instruments.

    Parameters
    ----------
    VISA_address: str
        The VISA address to query.
    VISA_index: int
        The address will be found from LIST_VISA node list with this index.

    Returns
    -------
    DataContainer
        optional: The input DataContainer is returned.
    """

    rm = pyvisa.ResourceManager("@py")

    if VISA_address == "":
        VISA_addresses = rm.list_resources()
        VISA_address = VISA_addresses[int(VISA_index)]

    # VISA descriptor to identify the test and measurement device
    scope = rm.open_resource(VISA_address)
    ident = str(scope.query("*IDN?"))
    print(ident, flush=True)

    return TextBlob(text_blob=ident)
