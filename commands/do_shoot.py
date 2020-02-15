# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Shoot(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print(str(robot) + "!!")
		Command.__init__(robot)
		self.requires(robot.shooter)
		self.shooter = robot.shooter
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		print("Shoot executed!!")
		self.shooter.shoot()

	def isFinished(self):
		# Once the the motor speed has reached the goal rpm, it can stop
		#XXX BELOW SHOULD GO IN CONDITIONAL COMMAND FOR FEEDER ACTIVATION
		return False

	def end(self):
		pass

	def interrupted(self):
		self.end
