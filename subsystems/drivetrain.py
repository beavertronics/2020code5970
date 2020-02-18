# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from Left_Motors import left_motors
from Right_Motors import right_motors

class Drivetrain(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:
			Do_Tank_Drive()

		'''
		super().__init__("drivetrain")
		print("drivetrain init! no seg fault please")

		self.robot = robot
		self.lm_inst = Left_Motors().left_motor_group
		self.rm_inst = Right_Motors().right_motor_group
		self.drive = DifferentialDrive(self.lm_inst, self.rm_inst)
		
	#XXX not sure if this is correct
	def initDefaultCommand(self):
		self.setDefaultCommand(Do_Tank_Drive(self.robot))

	def set_tank_speed(self, left_joy, right_joy):
		left_speed = left_joy.getY()
		right_speed = right_joy.getY()
		self.drive.tankDrive(left_speed, right_speed)

	def stop_robot(self):
		self.drive.tankDrive(0,0)

