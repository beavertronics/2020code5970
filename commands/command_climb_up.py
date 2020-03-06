# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from do_big_climb import Do_Big_Climb
from do_little_climb import Do_Little_Climb

class Command_Climb_Up(CommandGroup):

	def __init__(self, robot):
	    CommandGroup.__init__(self, name='Command_Climb_Up')
	    print("climber up command group init!!")
	    # retract as soon as released maybe
	    self.robot = robot
            self.addSequential(Do_Big_Climb(robot))
            self.addSequential(Do_Little_Climb(robot))
