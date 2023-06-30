from flojoy import flojoy, DataContainer, DefaultParams
import Phidget22
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *

def onVoltageRatioChange(self, voltageRatio):
    """Declaration of the Event handler, print Voltage variation for a channel"""
    print('VoltageRatio [' + str(self.getChannel()) + ']: ' + str(voltageRatio))

@flojoy
def PHIDGET22(default: DataContainer, default_parmas: DefaultParams, n_sensors: int=3, calibration1: float=0.015, calibration2: float=0.06) -> DataContainer:
    """Pressure Measurement with Phidget 22 sensors"""
    voltage: list[float] = []
    pressions: list[float] = []
    N = params['n_sensors']
    for i in range(0, N):
        voltageRatioInput = VoltageRatioInput()
        voltageRatioInput.setChannel(i)
        voltageRatioInput.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        voltageRatioInput.openWaitForAttachment(5000)
        volt_i: float = voltageRatioInput.getVoltageRatio()
        voltage.append(volt_i)
        pression_i: float = (volt_i - params['calibration1']) / params['calibration2']
        pressions.append(pression_i)
    return DataContainer(x={'a': voltage, 'b': pressions}, y=pressions)

@flojoy
def PHIDGET22_MOCK(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Mock Function for the node Phidget 22"""
    voltage: list[float] = []
    pressions: list[float] = []
    N = 4
    for i in range(0, N):
        volt_i: int = i * 10 + 4
        voltage.append(volt_i)
        pression_i: float = (volt_i - 0.015) / 0.06
        pressions.append(pression_i)
    return DataContainer(x={'a': voltage, 'b': pressions}, y=pressions)