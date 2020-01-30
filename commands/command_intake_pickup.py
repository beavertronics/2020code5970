# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from do_intake import Do_Intake
from do_four_bar import Do_Four_Bar
from do_four_bar_inside import Do_Four_Bar_Inside
from do_intake_delay import Do_Intake_Delay
from do_carrier import Do_Carrier

class Command_Intake_Pickup(CommandGroup):

	def __init__(self, robot):
		super().__init__()
		print("command group intake pickup initialized")
		#XXX have this happen while a button is pressed, retract as soon as released maybe
		self.robot = robot
		self.addSequential(Do_Four_Bar(robot))
		self.addSequential(Do_Intake_Delay(robot), 0.2)
		self.addSequential(Do_Intake(robot))
		self.addParallel(Do_Carrier(robot))
		self.addSequential(Do_Four_Bar_Inside(robot))

	def execute(self):
		pass

	def isFinished(self):
		return True

	def end(self):
		#self.addSequential(Do_Four_Bar_Inside(self.robot))
		pass

	def interrupted(self):
		self.end()
