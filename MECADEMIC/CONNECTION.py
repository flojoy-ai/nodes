import mecademicpy.robot as mdr
robot = mdr.Robot()
robot.Connect(address='192.168.0.100')

robot.ActivateRobot()
robot.Home()