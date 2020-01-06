# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem


class Shifters(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self):
		super().__init__()
		'''
		Command Dependencies:
			Shifter On/Off

		Initialize Pneumatics[shifters]
			Each solenoid is instantiated by 
			an "actuated" and "unactuated" command (on and off, respectively)
		'''
		self.shifter_solenoid_left = wpilib.Solenoid(0)
		self.shifter_solenoid_right = wpilib.Solenoid(1)

	def shifters_on(self):
		# actuate shifter solenoids; shift into high gear
		self.shifter_solenoid_left.set(True)
		self.shifter_solenoid_right.set(True)

	def shifters_off(self):
		# unactuate shifter solenoids; shift into low gear
		self.shifter_solenoid_left.set(False)
		self.shifter_solenoid_right.set(False)


