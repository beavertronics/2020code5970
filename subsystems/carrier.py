# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Carrier(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__()
		self.carrier_motor = wpilib.VictorSP(8)
		self.motor_speed = 0.314

	#Sets carrier motor to object's given motor speed, will be determined later
	def activate_carrier(self):
		speed = self.motor_speed
		self.carrier_motor.set(speed)
	
	def deactivate_carrier(self):
		self.carrier_motor.set(0)

	def reverse_carrier(self):
		speed = self.carrier_motor.get()
		new_speed = speed * -1
		self.carrier_motor.set(new_speed)
