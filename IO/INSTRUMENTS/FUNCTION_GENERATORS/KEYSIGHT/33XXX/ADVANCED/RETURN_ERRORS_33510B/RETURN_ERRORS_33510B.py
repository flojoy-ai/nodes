from flojoy import flojoy, DataContainer, TextBlob
import pyvisa
from typing import Optional, Literal
from qcodes.instrument_drivers.Keysight import Keysight33512B
from usb.core import USBError


@flojoy(
    deps={
        "pyvisa": "1.13.0",
        "pyusb": "1.2.1",
        "zeroconf": "0.102.0",
        "pyvisa_py": "0.7.0",
        "qcodes": "0.39.1",
    }
)
def RETURN_ERRORS_33510B(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The RETURN_ERRORS_33510B node returns error messages from the WFG.

    Error retrival is first-in-first-out (FIFO). Returning errors clears them
    from the instruments queue.

    If the "VISA_address" parameter is not specified the VISA_index will be
    used to find the address. The LIST_VISA node can be used to show the
    indicies of all available VISA instruments.

    This node should also work with compatible Keysight 33XXX wavefunction
    generators (although they are untested).

    Parameters
    ----------
    VISA_address: str
        The VISA address to query.
    VISA_index: int
        The address will be found from LIST_VISA node list with this index.

    Returns
    -------
    DataContainer
        TextBlob: Returns all errors in the WFG memory.
    """

    rm = pyvisa.ResourceManager("@py")
    if VISA_address == "":
        VISA_addresses = rm.list_resources()
        VISA_address = VISA_addresses[int(VISA_index)]

    try:
        ks = Keysight33512B(
            "ks",
            VISA_address,
            visalib="@py",
            device_clear=False,
        )
    except USBError as err:
        raise Exception(
            "USB port error. Trying unplugging+replugging the port."
        ) from err

    err_code, err_message = ks.error()
    errors = f"{err_code} {err_message}"

    return TextBlob(text_blob=errors)
