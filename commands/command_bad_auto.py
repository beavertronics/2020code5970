# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import CommandGroup
from wpilib.command import Command
from command_shoot import Command_Shoot
from do_bad_auto import Do_Bad_Auto

class Command_Bad_Auto(CommandGroup):
	''' 
	Robot should drive forward from baseline and line up 
	'''

	def __init__(self, robot):
		CommandGroup.__init__(self, name='Command_Bad_Auto')
		# Recognize as a wpilib command
		print("command_bad_auto init!!!!")
		# Command.__init__(self)
		self.requires(robot.drivetrain)
		self.drivetrain = robot.drivetrain
		self.addSequential(Do_Bad_Auto(robot))
		self.addSequential(Command_Shoot(robot))

#	
#	def initialize(self):
#		"""Called just before this Command runs the first time"""
#		pass
#	
#	def execute(self):
#		"""Called iteratively by Scheduler"""
#		print("BAD AUTO execute")
#
#	def isFinished(self):
#		# This is how running tank driving is prioritized
#		# In other words, runs til interrupted
#		return False
#
#	def end(self):
#		pass
#	
#	def interrupted(self):
#		self.end()
