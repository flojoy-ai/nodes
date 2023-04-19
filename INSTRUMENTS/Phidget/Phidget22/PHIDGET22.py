from flojoy import flojoy, DataContainer
import Phidget22
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *


def onVoltageRatioChange(self, voltageRatio):
    print("VoltageRatio [" + str(self.getChannel()) + "]: " + str(
        voltageRatio))  # Declaration of the Event handler, Voltage changement


@flojoy
def PHIDGET22(dc, params):
    voltage = []
    pressions = []
    N = int(params["n_sensors"])

    for i in range(0, N):
        voltageRatioInput = VoltageRatioInput()  # Creation of an instance of the VoltageRationInput class
        voltageRatioInput.setChannel(i)  # Set Channel for Communication with the Phidget Interface Kit
        voltageRatioInput.setOnVoltageRatioChangeHandler(
            onVoltageRatioChange)  # Assign the handler that will be called when the event occurs
        voltageRatioInput.openWaitForAttachment(5000)  # Open the Channel after event handler is set
        volt_i = voltageRatioInput.getVoltageRatio()  # Measure Voltage from the sensor
        voltage.append(volt_i)  # Add Voltage to the list of measurements

        pression_i = (volt_i - 0.015) / 0.06                      # Example of a Calibration to convert Voltage into pression
        pressions.append(pression_i)

    return DataContainer(x={"a": voltage, "b": pressions}, y=pressions)

@flojoy
def PHIDGET22_MOCK(dc, params):

    print('running mock version of PHIDGET SENSOR, number of sensor is set to 4 by default')

    voltage = []
    pressions = []
    N = 4

    for i in range(0, N):
        volt_i = i*10 + 4                                         # Scalar operation to modify data
        voltage.append(volt_i)                                    # Add Voltage to the list of measurements
        pression_i = (volt_i - 0.015) / 0.06                      # Example of a Calibration to convert Voltage into pression
        pressions.append(pression_i)

    return DataContainer(x={"a": voltage, "b": pressions}, y=pressions)