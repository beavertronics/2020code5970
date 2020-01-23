# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Four_Bar(Command):
	
	def __init__(self, robot):
		super().__init__()

		self.intake = robot.intake

	def initialize(self):
		print("four bar actuate")
	
	def execute(self):
		self.intake.fourbar_eject()
		return None

	def isFinished(self):
		return True

	def interrupted(self):
		print("Command 'do_four_bar' has been interrupted")
		self.end()
