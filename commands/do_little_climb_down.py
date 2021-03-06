# vim: set sw=4 noet ts=4 fileencoding=utf-8:

#XXX Still need to incorporate timing between big and little climb within a 
# command group
import wpilib
import wpilib.drive
from wpilib.command import Command
import time

class Do_Little_Climb_Down(Command):
	''' Changes the piston actuation of the unfolding upper stage. '''

	def __init__(self, robot):
		print("do_little_climb init")
		Command.__init__(self)
		self.requires(robot.climber)
		self.climber = robot.climber
#		self.climber.little_unactuate()
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.is_done = False
		self.old_time = time.time_ns()
		self.climber.little_unactuate()
	
	def execute(self):
		''' Called iteratively by Scheduler
		This reverses the position of the solenoid (hence the piston actuation)
		using the given piston '''
		#self.climber.reverse_solenoid(self.climber.littlum)
		t = time.time_ns()
		if (t - self.old_time) > 300000000: # units in ns
			self.is_done = True
		else:
			self.old_time = t
			self.is_done = False

	def isFinished(self):
		return self.is_done

#	def end(self):
#		self.climber.little_unactuate()
	
	#XXX Not sure if this behavior is desired
#	def interrupted(self):
#		self.climber.little_unactuate()
