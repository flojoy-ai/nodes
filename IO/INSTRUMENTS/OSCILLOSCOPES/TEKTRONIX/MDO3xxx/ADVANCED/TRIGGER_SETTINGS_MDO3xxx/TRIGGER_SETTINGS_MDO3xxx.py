from flojoy import flojoy, DataContainer, TextBlob
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
def TRIGGER_SETTINGS_MDO3xxx(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    num_channels: int = 4,
    query_set: Literal["query", "set"] = "query",
    edge_couplings: Literal[
        "unchanged", "ac", "dc", "hfrej", "lfrej", "noiserej"
    ] = "unchanged",
    trigger_types: Literal["unchanged", "edge", "logic", "pulse"] = "unchanged",
    edge_slope: Literal["unchanged", "rise", "fall", "either"] = "unchanged",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The TRIGGER_SETTINGS_MDO3xxx node sets advanced trigger settings.

    Note that "unchanged" will leave the settings unchanged.

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
    query_set: str
        Whether to query or set the triggering channel.
    edge_couplings: str
        Set the trigger edge coupling type.
    trigger_types: str
        Set to trigger on edge, logic, or pulses.
    edge_slope: str
        Set to trigger on positive, negative, or either slopes.

    Returns
    -------
    DataContainer
        TextBlob: Summary of trigger settings.
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

    if edge_couplings != "unchanged":
        match query_set:
            case "query":
                edge_couplings = tek.trigger.edge_coupling()
            case "set":
                tek.trigger.edge_coupling(edge_couplings)

    if trigger_types != "unchanged":
        match query_set:
            case "query":
                trigger_types = tek.trigger.type()
            case "set":
                tek.trigger.type(trigger_types)

    if edge_slope != "unchanged":
        match query_set:
            case "query":
                edge_slope = tek.trigger.edge_slope()
            case "set":
                tek.trigger.edge_slope(edge_slope)

    s = str(
        f"Edge coupling: {edge_couplings},\n"
        f"Trigger type: {trigger_types},\n"
        f"Edge slope: {edge_slope}"
    )

    tek.close()

    return TextBlob(text_blob=s)
