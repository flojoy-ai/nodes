from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument_drivers.Keithley.Keithley_2400 import Keithley2400


@flojoy(deps={"qcodes": "0.39.1", "pyvisa-py": "0.6.3", "pyserial": "3.5"})
def SET_VOLTAGE(
    default: Optional[DataContainer] = None,
    voltage: int = 2,
    voltage_range: int = 10,
    current_range: int = 1,
) -> OrderedPair:
    # Create an instance of the Keithley2400 instrument
    keithley = Keithley2400("keithley", "ASRL/dev/ttyUSB1::INSTR")

    # Connect to the instrument
    # keithley.reset()

    # Now you can use the instrument to perform measurements and control the power supply
    # For example, you can set the voltage range
    # keithley.ask(":SOUR:FUNC:MODE VOLT\n")
    keithley.rangev(voltage_range)  # Set the voltage range to 10V

    # You can also set the current range

    keithley.rangei(current_range)  # Set the current range to 1A

    # Set the voltage compliance
    # keithley.compliancev(5)  # Set the voltage compliance to 5V

    # Set the current compliance
    # keithley.compliancei(0.1)  # Set the current compliance to 0.1A

    # Set the output mode to voltage
    keithley.mode("VOLT")  # Set the mode to voltage

    # Set the sense mode to voltage
    keithley.sense("VOLT")  # Set the sense mode to voltage

    # Set the voltage level
    keithley.volt(voltage)  # Set the voltage level to 2V

    # Imprimer le statut de la sortie de l'instrument
    output_status = keithley.output()  # Lire le statut de la sortie
    print(f"Statut de la sortie : {output_status}")

    # Activer la sortie de l'instrument si nécessaire
    if output_status != "on":
        keithley.output("on")

    # Lire le courant
    current = keithley.curr()  # Read the current

    # Read the resistance
    resistance = keithley.resistance()  # Read the resistance

    # Disable the output
    keithley.output("off")  # Turn off the output

    # Disconnect from the instrument
    keithley.disconnect()

    return OrderedPair(voltages_values, current)
