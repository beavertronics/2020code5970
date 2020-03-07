# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
import time

class Do_Big_Climb_Test(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("do_big_climb TEST init!!")
		Command.__init__(self)
		self.requires(robot.climber_big)
		self.climber_big = robot.climber_big
#		self.climber_big.big_unactuate()
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.is_done = False
		self.climber_big.big_actuate()
		self.old_time = time.time_ns()
	
	def execute(self):
		''' Called iteratively by Scheduler
		This reverses the position of the solenoid (hence the piston actuation)
		using the given piston '''

		# This timer waits 3 something amount of nanoseconds before setting
		# is_done to True and calling isFinished on the command
		#self.climber_big.reverse_solenoid(self.climber_big.biggum)
		t = time.time_ns()
		if (t - self.old_time) > 300000000: # units in ns
			self.is_done = True
		else:
			self.old_time = t
			self.is_done = False

	def isFinished(self):
		return self.is_done

	def end(self):
		self.climber_big.big_unactuate()
	
	def interrupted(self):
		self.climber_big.big_unactuate()
