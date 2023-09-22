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
def SET_WAVEFORM_33510B(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    on_off: Literal["ON", "OFF"] = "OFF",
    query_set: Literal["query", "set"] = "query",
    channel: Literal["ch1", "ch2"] = "ch1",
    waveform: Literal[
        "SIN", "SQU", "TRI", "RAMP", "PULS", "PRBS", "NOIS", "ARB", "DC"
    ] = "SIN",
    frequency: float = 1e6,
    amplitude: float = 0.1,
    amplitude_unit: Literal["VPP", "VRMS", "DBM"] = "VPP",
    phase: float = 0,
    offset: float = 0,
    ramp_symmetry: float = 50,
    pulse_width: float = 20,
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The SET_WAVEFORM_33510B node is used to set waveform settings for a 33510B.

    The Keysight 33510B has a variety of waveform settings available.

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
    query_set: str
        Whether to query or set the waveform.
    channel: str
        The channel to set or query.
    waveform: str
        The type of waveform to use.
    frequency: float
        The voltage of the waveform to set, in Hz.
    amplitude: float
        The voltage of the waveform to set.
    amplitude_unit: str
        The voltage unit to set the waveform to.
    phase: float
        The phase to set the waveform to, in degrees.
    offset: float
        The voltage offset to set the waveform to, in volts.
    ramp_symmetry: float
        The ramp symmetry if the RAMP waveform is used, in percent.
    pulse_width: float
        The pulse width in nanoseconds if the PULS waveform is used.

    Returns
    -------
    DataContainer
        Scalar: The waveform measurement in the selected statistic mode.
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

    if on_off == "OFF":
        channel.output("OFF")

    match query_set:
        case "set":
            assert (
                -360.0 <= phase <= 360.0
            ), "The phase must be between -360 and 360 degrees."
            assert (
                0.0 <= ramp_symmetry <= 100.0
            ), "The ramp_symmetry must be between -0 and 100."
            assert (
                pulse_width >= 16
            ), "The pulse_width must be greater than or equal to 16 ns"

            channel.function_type(waveform)
            channel.amplitude_unit(amplitude_unit)
            channel.amplitude(amplitude)
            channel.phase(phase)
            channel.offset(offset)
            channel.frequency(frequency)
            if waveform == "RAMP":
                channel.ramp_symmetry(ramp_symmetry)
            if waveform == "PULS":
                channel.pulse_width(pulse_width)

            summary = f"{channel_str}: {waveform}, amplitude: {amplitude} "
            summary += f"{amplitude_unit}, frequency: {frequency} Hz"

        case "query":
            summary = f"{channel_str}: "
            waveform = channel.function_type()
            summary += f"waveform: {waveform}, \n"
            amplitude_unit = channel.amplitude_unit()
            amplitude = channel.amplitude()
            summary += f"amplitude: {amplitude} {amplitude_unit}, \n"
            frequency = channel.frequency()
            summary += f"frequency: {frequency} Hz, \n"
            phase = channel.phase()
            summary += f"phase: {phase}, \n"
            offset = channel.offset()
            summary += f"offset: {offset} V, \n"
            if waveform == "RAMP":
                channel.ramp_symmetry(ramp_symmetry)
                summary += f"ramp_symmetry: {ramp_symmetry}%, \n"
            if waveform == "PULS":
                channel.pulse_width(pulse_width)
                summary += f"pulse_width: {pulse_width}, \n"

    if on_off == "ON":
        channel.output("ON")

    ks.close()

    return TextBlob(text_blob=summary)
