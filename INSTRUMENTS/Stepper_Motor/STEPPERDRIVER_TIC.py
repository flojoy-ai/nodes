from flojoy import flojoy, DataContainer
from ticlib import TicUSB
from time import sleep


@flojoy
def STEPPERDRIVER_TIC(dc, params):
    
    tic=TicUSB()
    print("position du moteur: ")
    print(tic.get_error_occured())
    print(tic.get_current_position())
    print(tic.get_error_occured())
    
    tic.halt_and_set_position(0)
    tic.set_current_limit(0.1)
    tic.energize()
    tic.exit_safe_start()
    
    positions=[400,300,800,0]
    for position in positions :
        tic.set_target_position(position)
        while tic.get_current_position() != tic.get_target_position():
             sleep(0.1)
            
    tic.deenergize()
    tic.enter_safe_start()
    return DataContainer(x={"a": positions, "b": positions}, y=positions)


@flojoy
def STEPPERMOTOR_MOCK(dc, params):
    return DataContainer(x={"a": voltage, "b": pressions}, y=pressions)
