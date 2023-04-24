from flojoy import flojoy, DataContainer


@flojoy
def STEPPERMOTOR(dc, params):
    voltage = []
    pressions = []

    return DataContainer(x={"a": voltage, "b": pressions}, y=pressions)


@flojoy
def STEPPERMOTOR_MOCK(dc, params):
    return DataContainer(x={"a": voltage, "b": pressions}, y=pressions)
