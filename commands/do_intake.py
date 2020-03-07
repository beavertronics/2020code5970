# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
import time

class Do_Intake(Command):
	def __init__(self, robot):
		Command.__init__(self, name='Command_Intake')
		print("command_intake init!!")
		self.requires(robot.intake)
		self.intake = robot.intake
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
		#self.old_time = time.time_ns()
		#self.intake.fourbar_eject()
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		# This timer waits 3 something amount of nanoseconds before intaking
#		t = time.time_ns()
#		if (t - self.old_time) > 30000000:
#			self.intake.activate_intake()
#		else:
#			t = time.time_ns()
		self.intake.activate_intake()

	def isFinished(self):
		pass

	def end(self):
		self.intake.fourbar_inject()
		self.intake.deactivate_intake()
	
	def interrupted(self):
		self.end()
