# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Bad_Auto(Command):

	def __init__(self, robot):
		print("Do_Bad_Auto init!!")
		super().__init__()
		self.requires(robot.drivetrain)
		self.drivetrain = robot.drivetrain
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass

	def execute(self):
		"""Called iteratively by Scheduler"""
		print("Carrier activated!!")
		self.drivetrain.bad_auto_drive()

	def isFinished(self):
		return True

	def end(self):
		self.drivetrain.stop_robot()

	def interrupted(self):
		self.end()
