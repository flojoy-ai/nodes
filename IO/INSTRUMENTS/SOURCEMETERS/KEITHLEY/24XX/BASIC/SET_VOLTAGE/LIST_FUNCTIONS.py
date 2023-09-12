from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument_drivers.Keithley.Keithley_2400 import Keithley2400


@flojoy(deps={"qcodes": "0.39.1", "pyvisa-py": "0.6.3", "pyserial": "3.5"})
def LIST_FUNCTIONS(
    default: Optional[DataContainer] = None,
) -> OrderedPair:

    keithley = Keithley2400("keithley", "ASRL/dev/ttyUSB1::INSTR")

    methods = [method for method in dir(
        keithley) if callable(getattr(keithley, method))]
    print("Here are the methods")
    print(methods)

    return (default)
