# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Intake(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__()
		self.intake_motor = wpilib.VictorSP(7)
		
		# solenoid value arbitrary
		self.intake_solenoid_fourbar = wpilib.Solenoid(2)

	def fourbar_eject(self):
		''' Shoots the ball by controlling the flywheel motor '''
		self.intake_solenoid_fourbar.set(True)

	def fourbar_inject(self):
		self.intake_solenoid_fourbar.set(False)

	def activate_intake(self):
		# rpm = enconder output * arbitrary constant
		pwm_val = 1
		self.intake_motor.setSpeed(pwm_val)
	
	def backwards_intake(self):

