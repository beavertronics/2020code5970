# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Four_Bar_Inside(Command):

	def __init__(self, robot):
		#print("do_four_bar_inside init")
		Command.__init__(self)
		self.intake = robot.intake

	def initialize(self):
		#print("four bar back into robot!")

	def execute(self):
		self.intake.fourbar_inject()

	def isFinished(self):
		return True

	def interrupted(self):
		#print("Command 'do_four_bar_inside' has been interrupted")
		self.end()
