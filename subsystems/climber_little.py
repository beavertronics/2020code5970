# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Climber_Little(Subsystem):
	def __init__(self, robot):
		'''
		Unfolds climber using two stages of unfolding
		'''
		super().__init__("climber_little")
		# Subsystem.__init__(self, "climber")
	
		# Two pistons for the upper stage on same port
		self.littlum = wpilib.Solenoid(2)

	def little_actuate(self):
		''' Actuates the littlest stage of unfolding the climber via piston '''
		self.littlum.set(True)

	def little_unactuate(self):
		self.littlum.set(False)

	def reverse_solenoid(self, solenoid):
		''' Sets piston actuation to opposite of the current state '''
		state = solenoid.get()
		solenoid.set(not(state))

