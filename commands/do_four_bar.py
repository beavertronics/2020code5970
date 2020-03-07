# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Four_Bar(Command):
	
	def __init__(self, robot):
		print("do_four_bar init")
		Command.__init__(self)

		self.intake = robot.intake

	def initialize(self):
		pass
	
	def execute(self):
		self.intake.fourbar_eject()

	def isFinished(self):
		pass

	def end(self):
		self.intake.fourbar_inject()

	def interrupted(self):
		self.end()
