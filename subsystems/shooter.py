# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Shooter(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self):
		'''
		Command Dependencies:

		'''
		super().__init__()
		# Assumes four PWM ports for motors
		self.shooter_motor = wpilib.VictorSP(5)

	def shoot(self):
		''' Shoots the ball by controlling the flywheel motor '''
		#XXX Need to get pid_output 
		self.shooter_motor.set(pid_output)

