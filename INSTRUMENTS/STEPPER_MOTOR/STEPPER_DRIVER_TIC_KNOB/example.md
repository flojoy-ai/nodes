In this example app :

The ['STEPPER_DRIVER_TIC_KNOB'](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/STEPPER_MOTOR/STEPPER_DRIVER_TIC_KNOB/STEPPER_DRIVER_TIC_KNOB.py) controls a stepper motor movement with a TIC driver. It allows you to control the motor's rotation with a knob button. (From 0 to 100 is corresponding to a rotation between 0 and 360 degrees)

First, the user must define the current limitation, which depends on the motor's size and model.

After that, he can set the speed, the rotation, and the sleep time to create a specific movement for different applications.
Then, after clicking the 'Play' button, the motor will start moving.

After updating the knob position, click on play again to initiate a new movement.

- The ['END'](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/TERMINATORS/END/END.py) node terminates the process.

To create a repetitive movement, use the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) and the [`GOTO`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/GOTO/GOTO.py) nodes. 


