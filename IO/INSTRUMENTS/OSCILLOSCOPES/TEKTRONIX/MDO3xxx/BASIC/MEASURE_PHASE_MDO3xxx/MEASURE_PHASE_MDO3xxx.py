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
def MEASURE_PHASE_MDO3xxx(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    num_channels: int = 4,
    channel1: int = 0,
    channel2: int = 1,
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The MEASURE_PHASE_MDO3xxx node measures the phase between two channels.

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
    channel1: int
        The first channel.
    channel2: int
        The second channel.

    Returns
    -------
    DataContainer
        Scalar: The phase between the two channels.
    """

    assert channel1 != channel2, "The channels must not the same."

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

    tek.measurement[0].source1(f"CH{int(channel1 + 1)}")
    tek.measurement[0].source2(f"CH{int(channel2 + 1)}")
    value = tek.measurement[0].phase()

    tek.close()

    return Scalar(c=value)
