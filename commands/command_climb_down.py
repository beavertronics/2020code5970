# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from do_big_climb_down import Do_Big_Climb_Down
from do_little_climb_down import Do_Little_Climb_Down

class Command_Climb_Down(CommandGroup):

	def __init__(self, robot):
		CommandGroup.__init__(self, name='Command_Climb_Down')
		print("climber down command group init!!")
		# retract as soon as released maybe
		self.robot = robot
		self.addSequential(Do_Little_Climb_Down(robot))
		self.addSequential(Do_Big_Climb_Down(robot))
