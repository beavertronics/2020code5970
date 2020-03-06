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
		
		# constant indicating what speed the motor should go
		self.pwm_val = 0.5
		self.intake_motor = wpilib.VictorSP(4)
		self.fourbar = wpilib.Solenoid(0)

		print('intake init!!')

	def fourbar_eject(self):
		''' Shoots the ball by controlling the flywheel motor '''
		self.fourbar.set(True)

	def fourbar_inject(self):
		self.fourbar.set(False)

	# Currently sets to 0.5 speed
	def activate_intake(self):
		pwm_val = self.pwm_val
		self.intake_motor.set(pwm_val)
	
	def deactivate_intake(self):
		self.intake_motor.set(0)
	
	def backwards_intake(self):
		new_pwm_val = -1 * self.pwm_val
		self.intake_motor.set(new_pwm_val)

