# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
import time

class Do_Shoot(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("Do_Shoot init!!")
		Command.__init__(self)
		self.requires(robot.shooter)
		self.shooter = robot.shooter
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.shooter.shooter_motor.set(0.1)
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		self.shooter.shoot()

	def isFinished(self):
		pass

	def end(self):
		self.shooter.stop_shoot()

	def interrupted(self):
		self.end()
