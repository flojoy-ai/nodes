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
def ADVANCED_MEASUREMENTS_MDO3xxx(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    num_channels: int = 4,
    channel: int = 0,
    measurement: str = "period",
    statistic: Literal["instant", "mean", "max", "min", "stdev"] = "instant",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The ADVANCED_MEASUREMENTS_MDO3xxx node extracts waveform measurements from an MDO3xxx oscilloscope.

    This node is similar to MEASUREMENTS_MDO3xxx node but more measurements
    are availble. The available measurements are as follows:

    amplitude, area, burst, carea, cmean, crms, delay, distduty, extinctdb,
    extinctpct, extinctratio, eyeheight, eyewidth, fall, frequency, high, hits,
    low, maximum, mean, median, minimum, ncross, nduty, novershoot, nwidth,
    pbase, pcross, pctcross, pduty, peakhits, period, phase, pk2pk, pkpkjitter,
    pkpknoise, povershoot, ptop, pwidth, qfactor, rise, rms, rmsjitter,
    rmsnoise, sigma1, sigma2, sigma3, sixsigmajit, snratio, stddev, undefined,
    waveforms

    Also available are 5 statistic modes:
    instant, mean, max, min, and stdev where instant is a single measurement
    and stdev is the standard deviation of the mean.

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

    Returns
    -------
    DataContainer
        OrderedPair: The trace of the oscilloscope is
    """

    assert channel < num_channels, "Channel must be less than num_channels."

    measures = str(
        "amplitude, area, burst, carea, cmean, crms, delay, distduty, "
        "extinctdb, extinctpct, extinctratio, eyeheight, eyewidth, fall, "
        "frequency, high, hits, low, maximum, mean, median, minimum, ncross, "
        "nduty, novershoot, nwidth, pbase, pcross, pctcross, pduty, peakhits, "
        "period, phase, pk2pk, pkpkjitter, pkpknoise, povershoot, ptop, "
        "pwidth, qfactor, rise, rms, rmsjitter, rmsnoise, sigma1, sigma2, "
        "sigma3, sixsigmajit, snratio, stddev, undefined, waveforms"
    )

    assert (
        measurement in measures
    ), f"The select measurement ({measurement}) is not availble."

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

    measurement = getattr(tek.measurement[0], measurement)

    if statistic == "instant":
        value = measurement()
    else:
        measurement = getattr(measurement, statistic)
        value = measurement()

    tek.close()

    return Scalar(c=value)
