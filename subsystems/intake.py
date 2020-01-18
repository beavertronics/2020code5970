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
		#self.shooter_motor = wpilib.VictorSP(7)
		
	def intake_down(self):
		''' Shoots the ball by controlling the flywheel motor '''
		pass

	def activate_rollers(self):
		# rpm = enconder output * arbitrary constant
		rpm = 5 * 4
		return rpm

