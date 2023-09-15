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
    """The BURST_MODE_33510B node is used

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
        channel.burst_polarity(burst_polarity)  # Can be 'NORM' or 'INV'

    if on_off == "ON":
        channel.burst_state(on_off)
    ks.close()

    return TextBlob(text_blob=f"{channel_str} burst: {on_off}")
