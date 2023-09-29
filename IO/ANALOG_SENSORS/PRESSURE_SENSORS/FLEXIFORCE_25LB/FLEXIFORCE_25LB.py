from flojoy import flojoy, OrderedPair, DataContainer
from typing import Optional


@flojoy(deps={"pyserial": "3.5"})
def FLEXIFORCE_25LB(
    default: OrderedPair,
    calibration1: float = 0.015,
    calibration2: float = 0.06,
) -> OrderedPair:
    """The Flexiforce node allows you to convert voltages measured with the Phidget Interface Kit into pressures.

    Parameters
    ----------
    Calibration1 : float
        Calibration parameters to convert voltage into pressure.
    calibration2 : float
        Calibration parameters to convert voltage into pressure.
    """

    # Example of a Calibration to convert Voltage into pressions :
    pressions: list[float] = []
    sensor_num = default.x

    pression_i: float = (default.y - calibration1) / calibration2
    pressions.append(pression_i)

    return OrderedPair(sensor_num, pressions)
