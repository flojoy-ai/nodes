from flojoy import flojoy, DataContainer, Scalar
import pyvisa
from typing import Optional, Literal
from flojoy.instruments.tektronix.MDO30xx import TektronixMDO30xx


@flojoy(
    deps={
        "pyvisa": "1.13.0",
        "pyusb": "1.2.1",
        "zeroconf": "0.102.0",
        "pyvisa_py": "0.7.0",
        "qcodes": "0.39.1",
    }
)
def TERMINATION_MDO3xxx(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    num_channels: int = 4,
    channel: int = 0,
    termination: Literal["50 ohm", "75 ohm", "1M ohm"] = "50 ohm",
    query_set: Literal["query", "set"] = "query",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The TERMINATION_MDO3xxx node sets the termination ohms (or queries it).

    The termination is set by the output, and the set termination
    in the oscilloscope must match that value.

    Note that the termination is often called the "electrical impedance".

    Note that the 75 Ohm option is not compatible with all model numbers.

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
    channel: int
        The channel to query or set the impedance/termination.
    termination: str
        The ohm to which the termination impedance is set to.
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

    tek = TektronixMDO30xx(
        "MDO30xx",
        VISA_address,
        visalib="@py",
        device_clear=False,
        number_of_channels=num_channels,
    )

    match termination:
        case "50 ohm":
            termination = 50
        case "75 ohm":
            termination = 75  # Not compatible with all instruments.
        case "1M ohm":
            termination = 1e6

    match query_set:
        case "query":
            c = tek.channel[int(channel)].termination()
        case "set":
            tek.channel[int(channel)].termination(termination)
            c = termination

    tek.close()

    return Scalar(c=c)
