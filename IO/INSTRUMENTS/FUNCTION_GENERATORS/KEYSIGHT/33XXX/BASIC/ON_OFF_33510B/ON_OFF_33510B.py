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
def ON_OFF_33510B(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    on_off: Literal["ON", "OFF"] = "OFF",
    channel: Literal["ch1", "ch2"] = "ch1",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The ON_OFF_33510B node is used to turn the output on or off.

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
        Whether to turn the waveform generation to on or off.
    channel: str
        The channel to turn on or off.

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

    channel_str = channel
    channel = getattr(ks, channel)

    channel.output(on_off)

    ks.close()

    return TextBlob(text_blob=f"{channel_str}: {on_off}")
