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
def MEASUREMENTS_MDO3xxx(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    num_channels: int = 4,
    channel: int = 0,
    measurement: Literal["period", "frequency", "amplitude"] = "period",
    statistic: Literal["instant", "mean", "max", "min", "stdev"] = "instant",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The MEASUREMENTS_MDO3xxx node extracts waveform measurements from an MDO3xxx oscilloscope.

    This node can select from three different waveform measurements:
    frequency, period, and amplitude. Also available are 5 statistic modes:
    instant, mean, max, min, and stdev where instant is a single measurement
    and stdev is the standard deviation of the mean.

    Units are in seconds, Hz, and V for frequency, period, and amplitude respectively.

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
    measurement: str
        The measurement to extract from the scope.
    statistic: str
        The statistic mode to use for the measurement.

    Returns
    -------
    DataContainer
        Scalar: The waveform measurement in the selected statistic mode.
    """

    assert channel < num_channels, "Channel must be less than num_channels."

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

    tek.measurement[0].source1(f"CH{int(channel + 1)}")

    match measurement:
        case "frequency":
            chan = tek.measurement[0].source1()
            if statistic == "instant":
                value = tek.measurement[0].frequency()
            else:
                value = getattr(tek.measurement[0].frequency, statistic)
                value = value()
            unit = tek.measurement[0].frequency.unit
            print(f"Frequency of signal at channel {chan}: {value:.2E} {unit}")

        case "period":
            chan = tek.measurement[0].source1()
            if statistic == "instant":
                value = tek.measurement[0].period()
            else:
                value = getattr(tek.measurement[0].period, statistic)
                value = value()
            unit = tek.measurement[0].period.unit
            print(f"Period of signal at channel {chan}: {value:.2E} {unit}")

        case "amplitude":
            chan = tek.measurement[0].source1()
            if statistic == "instant":
                value = tek.measurement[0].amplitude()
            else:
                value = getattr(tek.measurement[0].amplitude, statistic)
                value = value()
            unit = tek.measurement[0].amplitude.unit
            print(f"Amplitude of signal at channel {chan}: {value:.2E} {unit}")

    tek.close()

    return Scalar(c=value)
