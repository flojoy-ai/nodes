from flojoy import flojoy, DataContainer, OrderedPair
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
def EXTRACT_TRACE_MDO3xxx(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    num_channels: int = 4,
    channel: int = 0,
    x_length: int = 5000,
    length_type: Literal["pixels", "nanoseconds"] = "pixels",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The EXTRACT_TRACE_MDO3xxx node extracts the trace from an MDO3xxx oscilloscope.

    The number of points in the x axis is defined by x_length and length_type
    parameters. A length_type of pixels and a x_length of 5000 will result in
    a trace with 5000 points. A length_type of nanoseconds instead results in
    a trace with a length of defined by the number of (nano)seconds.

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
    x_length: int
        The length of the trace to extract.
    length_type: select
        The units of the length specified in x_length: nanoseconds or pixels.

    Returns
    -------
    DataContainer
        OrderedPair: The trace of the oscilloscope is returned.
    """

    assert channel < num_channels, "Channel must be less than num_channels."

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

    match length_type:
        case "pixels":
            tek.channel[0].set_trace_length(x_length)
        case "nanoseconds":
            tek.channel[0].set_trace_time(x_length / 1e9)

    x = tek.channel[channel].waveform.trace_axis()
    y = tek.channel[channel].waveform.trace()

    tek.close()

    return OrderedPair(x=x, y=y)
