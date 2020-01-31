# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Carrier(Command):
	#XXX may want to inherit from TimedCommand instead of Command

	def __init__(self, robot):
		# Recognize as a wpilib command
		print(str(robot) + "!!")
		super().__init__()
		self.requires(robot.carrier)
		self.carrier = robot.carrier
	
	def initialize(self):
		"""Called just before this Command runs the first time"""

	def execute(self):
		"""Called iteratively by Scheduler"""
		print("Carrier activated!!")
		self.carrier.activate_carrier()

	def isFinished(self):
		#XXX Timed activation for correct carrying distance?
		return True

	def end(self):
		self.carrier.deactivate_carrier()

	def interrupted(self):
		self.end
