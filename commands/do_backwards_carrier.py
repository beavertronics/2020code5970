# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Backwards_Carrier(Command):
	''' This is now a manual command so we don't need a timed command etc.. '''

	def __init__(self, robot):
		Command.__init__(self)
		print("do_backwards_carrier init")
		self.requires(robot.carrier)
		self.carrier = robot.carrier
	
	def initialize(self):
		"""Called just before this Command runs"""
		pass

	def execute(self):
		self.carrier.stupid_carrier(-0.3)

	def isFinished(self):
		pass

	def end(self):
		self.carrier.deactivate_carrier()

	def interrupted(self):
		self.end()
