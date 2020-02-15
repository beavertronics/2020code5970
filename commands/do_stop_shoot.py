# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Stop_Shoot(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("do_stop_shoot init")
		Command.__init__(self)
		self.requires(robot.shooter)
		self.shooter = robot.shooter
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		print("Stop_shoot executed in init function!!")
		self.shooter.stop_shoot()	
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		pass

	def isFinished(self):
		return False

	def end(self):
		pass

	def interrupted(self):
		self.end()
