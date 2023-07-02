from flojoy import flojoy, DataContainer
import LabJackPython
import u3


@flojoy
def LABJACKU3(default: DataContainer, numbers: int = 1) -> DataContainer:
    """Takes a number of sensors as parameters and return their temperature measurement"""
    voltages: list[float] = []
    temperatures: list[float] = []
    temperatures_celsius: list[float] = []
    sensor_num: list[int] = []
    sensor_number: int = params["numbers"]
    d = u3.U3()
    d.configIO(FIOAnalog=255, EIOAnalog=0)
    for i in range(0, sensor_number):
        voltage: float = d.getAIN(i)
        temperature: float = voltage * 100.0
        temperature_celsius: float = (temperature - 32) / 1.8
        sensor_num.append(i + 1)
        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celsius.append(temperature_celsius)
    return DataContainer(
        type="ordered_pair",
        x={"a": sensor_num, "b": temperatures_celsius},
        y=temperatures_celsius,
    )


@flojoy
def LABJACKU3_MOCK(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Mock function for Labjack node"""
    voltages: list[float] = []
    temperatures: list[float] = []
    temperatures_celsius: list[float] = []
    sensor_number = 6
    voltage = 0.6
    for i in range(1, sensor_number):
        temperature: float = voltage * 100.0
        temperature_celsius: float = (temperature - 32) / 1.8
        voltages.append(voltage)
        temperatures.append(temperature)
        temperatures_celsius.append(temperature_celsius)
    return DataContainer(
        x={"a": temperatures, "b": temperatures_celsius}, y=temperatures_celsius
    )
