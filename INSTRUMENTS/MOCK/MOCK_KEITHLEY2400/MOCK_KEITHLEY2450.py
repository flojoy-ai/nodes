from flojoy import flojoy, Scalar, DataContainer
from qcodes.instrument_drivers.Keithley import Keithley2450
from typing import Optional

@flojoy(deps={"qcodes": "0.39.1", "pyvisa-sim": "0.5.1"})
def MOCK_KEITHLEY2450(
    default: Optional[DataContainer] = None,
    voltage: float = 0.0,
) -> Scalar:
    """Note this node is for testing purposes only.

    The KEYTHLEY2450 node mocks the instrument KEYTHLEY 2450.
    The KEYTHLEY 2450 is the voltage source.

    Parameters
    ----------
    voltage : float
        
    Returns
    -------
    Scalar
        
    """
    keith_sim = Keithley2450(
        "keith_sim",
        address="GPIB::1::INSTR",
        pyvisa_sim_file="Keithley_2450.yaml",
    )

    idn_dict = keith_sim.get_idn()
    print(f"Connected to mock instrument: {idn_dict}")

    print(f"Current voltage: {idn_dict} dB")

    return Scalar(c=keith_sim.VOLT)
