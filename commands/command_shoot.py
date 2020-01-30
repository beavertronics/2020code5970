# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from do_shooter import Do_Shooter
from do_carrier import Do_Carrier
from do_feeder import Do_Feeder

class Command_Shoot(CommandGroup):
	def __init__(self, robot):
		# Recognize as a wpilib command
		print(str(robot) + "!!")
		super().__init__()
		print("command group shoot initialized")
		self.robot = robot
		self.addSequential(Do_Carrier(robot))
		self.addSequential(Do_Shoot(robot))
		self.addSequential(Do_Feeder(robot))
		self.addSequential(Do_Stop_Shoot(robot))
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		pass

	def isFinished(self):
		return True

	def end(self):
		pass

	def interrupted(self):
		self.end
