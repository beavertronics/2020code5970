# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Intake(Command):
	def __init__(self, robot):
		Command.__init__(self, name='Command_Intake')
		print("command_intake init!!")
		self.requires(robot.intake)
		self.intake = robot.intake
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		self.intake.fourbar_eject()
		self.intake.activate_intake()

	def isFinished(self):
		pass

	def end(self):
		self.intake.fourbar_inject()
		self.intake.deactivate_intake()
	
	def interrupted(self):
		self.end()
