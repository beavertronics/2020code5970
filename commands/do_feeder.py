# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Feeder(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print(str(robot) + "!!")
		Command.__init__(self)
		self.requires(robot.feeder)
		self.feeder = robot.feeder

	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		print("Feeder activated!!")
		self.feeder.activate_feeder()

	def isFinished(self):
		#XXX Do we need some kind of delay in here so it goes the proper distance?
		return False

	def end(self):
		self.feeder.deactivate_feeder()
	
	def interrupted(self):
		self.end
