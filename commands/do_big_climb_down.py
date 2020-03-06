# vim: set sw=4 noet ts=4 fileencoding=utf-8:

#XXX Still need to incorporate timing between big and little climb within a 
# command group
import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Big_Climb_Down(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("do_big_climb init!!")
		Command.__init__(self)
		self.requires(robot.climber)
		self.climber = robot.climber
#		self.climber.big_actuate()
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.climber.big_unactuate()
	
	def isFinished(self):
		return True
