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
		pwm_val = 0.5

		# resource already allocated -- multiple references to pwm 7
		# self.intake_motor = wpilib.VictorSP(7)
		self.intake_motor = wpilib.VictorSP(4)
		
		# solenoid value arbitrary
		self.fourbar = wpilib.Solenoid(2)

	def fourbar_eject(self):
		''' Shoots the ball by controlling the flywheel motor '''
		self.fourbar.set(True)

	def fourbar_inject(self):
		self.fourbar.set(False)

	def activate_intake(self):
		self.intake_motor.set(pwm_val)
	
	def backwards_intake(self):
		new_pwm_val = -1 * pwm_val
		self.intake_motor.set(new_pwm_val)

