# vim: set sw=4 noet ts=4 fileencoding=utf-8:

#XXX Still need to incorporate timing between big and little climb within a 
# command group
import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Big_Climb(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print(str(robot) + "!!")
		super().__init__()
		self.requires(robot.climber)
		self.climber = robot.climber
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		''' Called iteratively by Scheduler
		This reverses the position of the solenoid (hence the piston actuation)
		using the given piston '''
		print("Do_Big_Climb execute!!")
		self.climber.reverse_solenoid(self.climber.biggum)

	def isFinished(self):
		return True

	def end(self):
		pass
	
	#XXX Not sure if this behavior is desired
	def interrupted(self):
		self.big_unactuate()
