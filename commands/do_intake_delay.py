# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Intake_Delay(Command):

	def __init__(self, robot):
		#print("do_intake_delay init")
		Command.__init__(self)

	def initialize(self):
		pass

	def execute(self):
		pass

	def isFinished(self):
		return True

	def interrupted(self):
		self.end()
