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
def OUTPUT_SYNC_33510B(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    on_off: Literal["ON", "OFF"] = "OFF",
    channel: Literal["1", "2"] = "1",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The OUTPUT_SYNC_33510B node is used sync multiple outputs phases.

    Can only be turned on for one channel.

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
    on_off: str
        Whether to turn the waveform phase syncing on or off.
    channel: str
        The channel to use as the baseline phase.

    Returns
    -------
    DataContainer
        TextBlob: ON or OFF depending on on_off value.
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

    ks.sync.source(int(channel))
    match on_off:
        case "OFF":
            ks.sync.output("OFF")
        case "ON":
            ks.sync.output("ON")
            ks.write("PHAS:SYNC")

    ks.close()

    return TextBlob(text_blob=f"CH{channel} sync: {on_off}")
