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
		print("command_bad_auto init!!")
		self.requires(robot.drivetrain)
		self.drivetrain = robot.drivetrain
		self.addSequential(Do_Bad_Auto(robot))
		self.addSequential(Command_Shoot(robot))

