from flojoy import flojoy, OrderedPair
from typing import Optional
from Phidget22.Devices.VoltageRatioInput import VoltageRatioInput


def onVoltageRatioChange(self, voltageRatio):
    """Declaration of the Event handler, print Voltage variation for a channel"""
    print("VoltageRatio [" + str(self.getChannel()) + "]: " + str(voltageRatio))


@flojoy(deps={"Phidget22": "1.14.20230331"})
def PHIDGET22(
    default: Optional[OrderedPair] = None,
    n_sensors: int = 1,
    calibration1: float = 0.015,
    calibration2: float = 0.06,
) -> OrderedPair:
    """
    The node Phidget allows you to record pressures from Flexiforce sensors using a Phidget InterfaceKit.

    Parameters
    -----------
    n_sensors: int
         Defines the number of pressure sensors connected to the Phidget Interface Kit.
    calibration1: float
    calibration2: float
        Calibration parameters to convert voltage into pressure.
    """
    voltage: list[float] = []
    pressions: list[float] = []
    sensor_num: list[int] = []

    for i in range(0, n_sensors):
        sensor_num.append(i + 1)
        # Creation of an instance of the VoltageRationInput class
        voltage_ratio_input = VoltageRatioInput()
        # Set Channel for Communication with the Phidget Interface Kit :
        voltage_ratio_input.setChannel(i)
        # Assign the handler that will be called when the event occurs :
        voltage_ratio_input.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        # Open the Channel after event handler is set :
        voltage_ratio_input.openWaitForAttachment(5000)

        volt_i: float = (
            voltage_ratio_input.getVoltageRatio()
        )  # Measure Voltage from the sensor
        voltage.append(volt_i)  # Add Voltage to the list of measurements

        # Example of a Calibration to convert Voltage into pressions :
        pression_i: float = (volt_i - calibration1) / calibration2
        pressions.append(pression_i)

    results = OrderedPair(x=sensor_num, y=pressions)

    return results
