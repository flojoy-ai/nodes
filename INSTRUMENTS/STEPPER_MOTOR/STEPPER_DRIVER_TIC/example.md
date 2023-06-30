This is a tutorial for using the nodes called Stepper Motor driver Tic and Stepper Driver motor Tic Knob in order to control a motor with the Flojoy App

**Hardware required :**

- A Motor (Nema 15-23)
- A Tic motor driver (All models are available and should work with these nodes) -- TIC T825 was used for experimentation. 
- A Power Supply wich enough power to run the driver and the motor. (You'll need to setup the good current value depending on the motor size you are using)
- Connections cables (USB, Electronic cables)

![TIC Driver Connections](https://res.cloudinary.com/dhopxs1y3/image/upload/v1683653875/steppermotor_z7yaly.jpg)
*Connection between the computer, the Tic driver, the stepper motor and the power supply* 


**Software required :**

Flojoy software running (Go to the page -- Getting started/Installation)


**Node Management :**
- Input data : None
- Output node : End (To stop the process)

You don't need to have a node placed before the stepper motor nodes because the only data needed by the nodes is set up with the parameters. 

**Parameters : **

The Stepper Driver Tic node allows you to set 2 different speeds and 4 positions for the stepper motor. 
The motor will move to the first two positions with first speed parameters and then move to position 3 and 4 with the second speed parameters 
(You can set the same speed for both and reduce the number of movement by settting the same position for 2,3 and 4)

![Stepper node classic](https://res.cloudinary.com/dhopxs1y3/image/upload/v1683653875/steppernode_mssx65.png)
*Flojoy interface with the classic node* 


At the end of the process the stepper motor will be placed in the last position set up and wait for a new parameters for the next movement. 
It should be possible to use these nodes with the LOOP node in order to make a repetitive movement with the motor. 

