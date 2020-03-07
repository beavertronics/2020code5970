# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
import time

class Do_Little_Climb(Command):
	''' Changes the piston actuation of the unfolding upper stage. '''

	def __init__(self, robot):
		print("do_little_climb init")
		Command.__init__(self)
		self.requires(robot.climber_little)
		self.climber_little = robot.climber_little
#		self.climber_little.little_unactuate()
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.is_done = False
		self.climber_little.little_actuate()
		self.old_time = time.time_ns()
	
	def execute(self):
		''' Called iteratively by Scheduler
		This reverses the position of the solenoid (hence the piston actuation)
		using the given piston '''
		#self.climber_little.reverse_solenoid(self.climber_little.littlum)
		t = time.time_ns()
		if (t - self.old_time) > 300000000: # units in ns
			self.is_done = True
		else:
			self.old_time = t
			self.is_done = False

	def isFinished(self):
		return self.is_done

	def end(self):
		self.climber_little.little_unactuate()
	
	def interrupted(self):
		self.climber_little.little_unactuate()
