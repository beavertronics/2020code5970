# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Feeder(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__("feeder")
		
		#XXX 0, 1, 2, 3 not wired 
		#XXX 4 is intake? 
		#XXX 5 is CARRIER
		#XXX 6 is shooter
		#XXX 7 is winch?
		#XXX 8 is FEEDER?
		self.feeder_motor = wpilib.VictorSP(8)
		# Backwards is apparently forwards
		self.motor_speed = -0.5

	# Sets feeder motor to object's given motor speed, will be determined later
	def activate_feeder(self):
		# This is like this because seg faults
		speed = self.motor_speed
		self.feeder_motor.setSpeed(speed)

	def deactivate_feeder(self):
		self.feeder_motor.setSpeed(0)

