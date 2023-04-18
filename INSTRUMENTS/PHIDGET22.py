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

    for i in range(1,N):
        voltageRatioInput = VoltageRatioInput()
        voltageRatioInput.setChannel(i)
        voltageRatioInput.setOnVoltageRatioChangeHandler(
            onVoltageRatioChange)  # Assign the handler that will be called when the event occurs
        voltageRatioInput.openWaitForAttachment(5000)  # Open the Channel after event handler is set
        volt_i = voltageRatioInput.getVoltageRatio()
        voltage.append(volt_i)
        pression_i = (volt_i - 0.015) / 0.06
        pressions.append(pression_i)

    # voltageRatioInput1 = VoltageRatioInput()
    # voltageRatioInput2 = VoltageRatioInput()
    # voltageRatioInput3 = VoltageRatioInput()
    # voltageRatioInput4 = VoltageRatioInput()  # This is creating 4 instances of VoltageRatioInput Class

    # voltageRatioInput1.setChannel(1)  # For each instance we call the function setChannel to set a real channel to our instance
    # voltageRatioInput2.setChannel(2)
    # voltageRatioInput3.setChannel(3)
    # voltageRatioInput4.setChannel(4)

    # voltageRatioInput1.setOnVoltageRatioChangeHandler(onVoltageRatioChange)  # Assign the handler that will be called when the event occurs
    # voltageRatioInput2.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
    # voltageRatioInput3.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
    # voltageRatioInput4.setOnVoltageRatioChangeHandler(onVoltageRatioChange)

    # voltageRatioInput1.openWaitForAttachment(5000)  # Open the Channel after event handler is set
    # voltageRatioInput2.openWaitForAttachment(5000)
    # voltageRatioInput3.openWaitForAttachment(5000)
    # voltageRatioInput4.openWaitForAttachment(5000)

    #try:
    #    input("Press Enter to Stop\n")
    #except (Exception, KeyboardInterrupt):
    #    pass

    return DataContainer(x={"a": voltage, "b": pressions}, y=pressions)

    # We remove the value from the calibration measurement in order to start with null pressure when no vacuum is applied.

    # volt1 = voltageRatioInput1.getVoltageRatio()
    # pression1= (volt1-0.017)/0.06                         # Conversion from V to Kpa
    # pression1 = (volt1 - 0.015) / 0.06
    # print('Voltage 1 : ', volt1, 'V')

    # volt2 = voltageRatioInput2.getVoltageRatio()
    # pression2= (volt2-0.038)/0.06
    # pression2 = (volt2 - 0.002 / 0.06)
    # print('Voltage 2 : ', volt2, 'V')

    # volt3 = voltageRatioInput3.getVoltageRatio()
    # pression3= (volt3-0.026)/0.06
    # pression3 = (volt3) / 0.06
    # print('Voltage 3 : ', volt3, 'V')

    # volt4 = voltageRatioInput4.getVoltageRatio()
    # pression4= (volt4-0.034)/0.06
    # pression4 = (volt4) / 0.06
    # print('Voltage 4 : ', volt3, 'V')

    # print("Pression : ", 'P1 =', round(pression1, 3), "[Kpa] ,", 'P2=', round(pression2, 3), "[Kpa] ,", 'P3=',
    #      round(pression3, 3), "[Kpa] ,", 'P4=', round(pression4, 3), "[Kpa] ,")

    # voltageRatioInput1.close()
    # voltageRatioInput2.close()
    # voltageRatioInput3.close()
    # voltageRatioInput4.close()
