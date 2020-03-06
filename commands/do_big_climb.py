# vim: set sw=4 noet ts=4 fileencoding=utf-8:

#XXX Still need to incorporate timing between big and little climb within a 
# command group
import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Big_Climb(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("do_big_climb init!!")
		Command.__init__(self)
		self.requires(robot.climber)
		self.climber = robot.climber
		self.climber.big_actuate()
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		''' Called iteratively by Scheduler
		This reverses the position of the solenoid (hence the piston actuation)
		using the given piston '''
		#self.climber.reverse_solenoid(self.climber.biggum)
		self.climber.big_unactuate()

	def isFinished(self):
		pass

	def end(self):
		self.climber.big_actuate()
	
	def interrupted(self):
		self.climber.big_actuate()
