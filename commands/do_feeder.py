# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Feeder(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("do_feeder init")
		Command.__init__(self)
		self.requires(robot.feeder)
		self.feeder = robot.feeder

	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		self.feeder.activate_feeder()

	def isFinished(self):
		pass

	def end(self):
		self.feeder.deactivate_feeder()
	
	def interrupted(self):
		self.end()
