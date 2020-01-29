# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Carrier(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print(str(robot) + "!!")
		super().__init__()
		self.requires(robot.carrier)
		self.carrier = robot.carrier
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		# Starts by being off before turning on
		self.carrier.deactivate_motor()
		self.carrier.activate_motor()

	def execute(self):
		"""Called iteratively by Scheduler"""
		pass

	def isFinished(self):
		return False

	def end(self):
		# Turn it off when you're done
		self.carrier.deactivate_motor()

	def interrupted(self):
		self.end
