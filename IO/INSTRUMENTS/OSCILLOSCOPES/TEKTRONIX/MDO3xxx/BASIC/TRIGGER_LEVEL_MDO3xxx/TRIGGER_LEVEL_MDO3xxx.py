from flojoy import flojoy, DataContainer, Scalar
import pyvisa
from typing import Optional, Literal
from flojoy.instruments.tektronix.MDO30xx import TektronixMDO30xx
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
def TRIGGER_LEVEL_MDO3xxx(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    num_channels: int = 4,
    trigger_volts: float = 0.1,
    query_set: Literal["query", "set"] = "query",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The TRIGGER_LEVEL_MDO3xxx node sets the trigger voltage (or queries it).

    The trigger voltage is the level at which an oscilloscope will find the
    start of a signal.

    If the "VISA_address" parameter is not specified the VISA_index will be
    used to find the address. The LIST_VISA node can be used to show the
    indicies of all available VISA instruments.

    This node should also work with compatible Tektronix scopes (untested):
    MDO4xxx, MSO4xxx, and DPO4xxx.

    Parameters
    ----------
    VISA_address: str
        The VISA address to query.
    VISA_index: int
        The address will be found from LIST_VISA node list with this index.
    num_channels: int
        The number of channels on the instrument that are currently in use.
    trigger_volts: float
        The voltage to set the triggering level to.
    query_set: str
        Whether to query or set the triggering voltage.

    Returns
    -------
    DataContainer
        Scalar: The triggering voltage.
    """

    rm = pyvisa.ResourceManager("@py")
    if VISA_address == "":
        VISA_addresses = rm.list_resources()
        VISA_address = VISA_addresses[int(VISA_index)]

    try:
        tek = TektronixMDO30xx(
            "MDO30xx",
            VISA_address,
            visalib="@py",
            device_clear=False,
            number_of_channels=num_channels,
        )
    except USBError as err:
        raise Exception(
            "USB port error. Trying unplugging+replugging the port."
        ) from err

    match query_set:
        case "query":
            volts = tek.trigger.level()
            c = volts
        case "set":
            tek.trigger.level(trigger_volts)
            c = trigger_volts

    tek.close()

    return Scalar(c=c)
