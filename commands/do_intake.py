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
		self.old_time = time.time_ns()
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		self.intake.fourbar_eject()
		# This timer waits 3 something amount of nanoseconds before setting
		# is_done to True and calling isFinished on the command
		#self.climber_big.reverse_solenoid(self.climber_big.biggum)
		t = time.time_ns()
		#while not((t - self.old_time) > 300000000): # units in ns
		#	self.old_time = t

		self.intake.activate_intake()

	def isFinished(self):
		pass

	def end(self):
		self.intake.fourbar_inject()
		self.intake.deactivate_intake()
	
	def interrupted(self):
		self.end()
