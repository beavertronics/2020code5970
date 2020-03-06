# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Command_Intake(Command):
	def __init__(self, robot):
		Command.__init__(self, name='Command_Intake')
		print("command_intake init!!")
		self.requires(robot.intake)
		self.requires(robot.carrier)
		self.intake = robot.intake
		self.carrier = robot.carrier
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		# Continuously sets motor speed to joystick inputs w/ Scheduler
		pass

	def isFinished(self):
		# This is how running tank driving is prioritized
		# In other words, runs til interrupted
		return False

	def end(self):
		# Stop motors when ending command
		pass
	
	def interrupted(self):
		pass
