# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
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
		self.carrier.activate_carrier()

	def execute(self):
		"""Called iteratively by Scheduler"""
		pass

	def isFinished(self):
		#XXX Do we need some kind of delay in here so it goes the proper distance?
		return False

	def end(self):
		self.carrier.deactivate_carrier()

	def interrupted(self):
		self.end
