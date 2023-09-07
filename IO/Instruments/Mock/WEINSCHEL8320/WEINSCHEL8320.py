from flojoy import flojoy, Scalar, DataContainer
from qcodes.instrument_drivers.weinschel import Weinschel8320
from typing import Optional


@flojoy(deps={"qcodes": "0.39.1", "pyvisa-sim": "0.5.1"})
def WEINSCHEL8320(
    default: Optional[DataContainer] = None,
    attenuation: int = 10,
) -> Scalar:
    """Note this node is for testing purposes only.

    The WEINSCHEL8320 node mocks the instrument WEINSCHEL 8320.
    The Weinschel 8320 attenuates the input signal.

    Parameters
    ----------
    attenuation : int
        Value that the instrument would attenuate the input signal (mocked).

    Returns
    -------
    Scalar
        c: attenuation value
    """

    wein_sim = Weinschel8320(
        "wein_sim",
        address="GPIB::1::INSTR",
        pyvisa_sim_file="Weinschel_8320.yaml",
    )

    idn_dict = wein_sim.IDN()
    print(f"Connected to mock instrument: {idn_dict}")

    wein_sim.attenuation(attenuation)

    # Get the current attenuation value
    attenuation_value = wein_sim.attenuation()

    # Print the current attenuation value
    print(f"Current attenuation: {attenuation_value} dB")

    return Scalar(c=attenuation_value)
