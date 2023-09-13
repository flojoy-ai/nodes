from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument_drivers.Keithley.Keithley_2400 import Keithley2400


@flojoy(deps={"qcodes": "0.39.1", "pyvisa-py": "0.6.3", "pyserial": "3.5"})
def SET_CURRENT(
    default: Optional[DataContainer] = None,
    current: int = 1,
    voltage_range: int = 10,
    current_range: int = 4,
    compliance_voltage: int = 10,
    compliance_current: int = 1,
) -> OrderedPair:
    # Create an instance of the Keithley2400 instrument
    keithley = Keithley2400("keithley", "ASRL/dev/ttyUSB1::INSTR")

    keithley.rangev(voltage_range)  # Set the voltage range
    keithley.rangei(current_range)  # Set the current range

    keithley.compliancev(compliance_voltage)  # Set the voltage compliance
    keithley.compliancei(compliance_current)  # Set the current compliance

    keithley.mode("CURR")  # Set the mode to Current
    keithley.sense("VOLT")  # Set the sense mode to voltage

    keithley.curr(current)  # Set the current
    voltage_measured = keithley.volt()  # Read the voltage

    # Disable the output
    keithley.output("off")  # Turn off the output

    # Disconnect from the instrument
    keithley.disconnect()

    return OrderedPair(current, voltage_measured)
