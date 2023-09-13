from flojoy import flojoy, DataContainer

# The most basic node, for tests

@flojoy
def MECADEMIC():
    return DataContainer(type='extra', extra=0)
