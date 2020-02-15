# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Feeder(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__("carrier")
		
		self.feeder_motor = wpilib.VictorSP(5)
		self.motor_speed = 0.3

	# Sets feeder motor to object's given motor speed, will be determined later
	def activate_feeder(self):
		speed = self.motor_speed
		self.feeder_motor.setSpeed(speed)

	def deactivate_feeder(self):
		self.feeder_motor.setSpeed(0)

