# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Intake(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__("intake")
		# Subsystem.__init__(self, "intake")
		
		# constant, just indicates what speed the intake motor should go
		self.pwm_val = 0.5

		# 7 Supposedly works
		self.intake_motor = wpilib.VictorSP(7)
		
		#XXX solenoid value arbitrary
		self.fourbar = wpilib.Solenoid(2)

	def fourbar_eject(self):
		''' Shoots the ball by controlling the flywheel motor '''
		self.fourbar.set(True)

	def fourbar_inject(self):
		self.fourbar.set(False)

	# Currently sets to 0.5 speed
	def activate_intake(self):
		self.intake_motor.set(self.pwm_val)
	
	def backwards_intake(self):
		new_pwm_val = -1 * self.pwm_val
		self.intake_motor.set(new_pwm_val)

