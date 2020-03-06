# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Climber(Subsystem):
	def __init__(self, robot):
		'''
		Unfolds climber using two stages of unfolding
		'''
		super().__init__("climber")
		# Subsystem.__init__(self, "climber")
	
		# Note to self: Biggum is two pistons on the lower stage which are
		# currently on the same solenoid port
		self.biggum = wpilib.Solenoid(1)
		# Two pistons for the upper stage on same port
		self.littlum = wpilib.Solenoid(2)
		
	def big_actuate(self):
		''' Actuates the biggest stage of unfolding the climber via piston '''
		self.biggum.set(True)
	
	def big_unactuate(self):
		self.biggum.set(False)

	def little_actuate(self):
		''' Actuates the littlest stage of unfolding the climber via piston '''
		self.littlum.set(False)

	def little_unactuate(self):
		self.littlum.set(True)

	def reverse_solenoid(self, solenoid):
		''' Sets piston actuation to opposite of the current state '''
		state = solenoid.get()
		solenoid.set(not(state))

