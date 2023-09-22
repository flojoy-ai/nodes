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
def BURST_MODE_33510B(
    VISA_address: Optional[str],
    VISA_index: Optional[int] = 0,
    on_off: Literal["ON", "OFF"] = "OFF",
    channel: Literal["ch1", "ch2"] = "ch1",
    trigger_source: Literal["EXT", "IMM", "TIM"] = "TIM",
    trigger_delay: float = 0,
    trigger_slope: Literal["POS", "NEG"] = "POS",
    trigger_timer: float = 1e-3,
    burst_mode: Literal["N Cycle", "Gated"] = "N Cycle",
    burst_ncycles: int = 1,
    burst_phase: float = 0,
    burst_polarity: Literal["NORM", "INV"] = "NORM",
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The BURST_MODE_33510B node is used to turn the Burst mode on or off.

    You can set various settings for the triggering of the bursts as well.
    The burst mode is way to have signals come in "bursts" that are triggered
    externally or with a timer for instance.

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
        Turn the burst mode on or off.
    channel: str
        The channel to modify the burst mode for.
    trigger_source: str
        Set the trigger_source (e.g. externally or timed).
    trigger_delay: float
        Delay the burst by this number of seconds after a trigger.
    trigger_slope: str
        If triggering is external, trigger on a positive or negative slope.
    burst_mode: str
        Set the burst mode for the WFG.
    burst_ncycles: int
        How many cycles to have in one burst.
    burst_phase: float
        What phase to start the burst with, in degrees.
    burst_polarity: str
        The polarity of the burst in Gated mode, normal or inverted.

    Returns
    -------
    DataContainer
        TextBlob: summary of burst mode settings.
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

    channel.trigger_source(trigger_source)
    assert trigger_delay >= 0, "trigger_delay must be greater than or equal to zero."
    channel.trigger_delay(trigger_delay)

    if trigger_source == "EXT":
        channel.trigger_slope(trigger_slope)

    if trigger_source == "TIM":
        assert (
            trigger_timer >= 1e-6
        ), "trigger_timer must be greater than or equal to 1us."
        channel.trigger_timer(trigger_timer)

    if on_off == "OFF":
        channel.burst_state(on_off)

    assert (
        -360.0 <= burst_phase <= 360.0
    ), "The phase must be between -360 and 360 degrees."
    channel.burst_mode(burst_mode)
    channel.burst_phase(burst_phase)

    if burst_mode == "N Cycle":
        assert burst_ncycles > 0, "burst_ncycles must be greater than 0."
        channel.burst_ncycles(burst_ncycles)

    if burst_mode == "Gated":
        channel.burst_polarity(burst_polarity)

    if on_off == "ON":
        channel.burst_state(on_off)
    ks.close()

    return TextBlob(text_blob=f"{channel_str} burst: {on_off}")
