from flojoy import flojoy, Scalar, DataContainer
from qcodes.instrument_drivers.Keithley import Keithley2400
from typing import Optional

@flojoy(deps={"qcodes": "0.39.1", "pyvisa-sim": "0.5.1"})
def MOCK_KEITHLEY2400(
    default: Optional[DataContainer] = None,
    voltage: int = 0.0,
) -> Scalar:
    """Note this node is for testing purposes only.

    The KEYTHLEY2400 node mocks the instrument KEYTHLEY 2400.
    The KEYTHLEY 2400 is the voltage source.

    Parameters
    ----------
    voltage : int
        

    Returns
    -------
    Scalar
        
    """
    keith_sim = Keithley2400(
        "keith_sim",
        address="GPIB::1::INSTR",
        pyvisa_sim_file="Keithley_2400.yaml",
    )

    idn_dict = keith_sim.IDN()
    print(f"Connected to mock instrument: {idn_dict}")

    keith_sim._volt_parser("9.0")
