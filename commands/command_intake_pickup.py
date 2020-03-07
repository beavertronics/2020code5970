# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from do_intake import Do_Intake
#from do_four_bar import Do_Four_Bar
#from do_four_bar_inside import Do_Four_Bar_Inside
#from do_intake_delay import Do_Intake_Delay
from do_carrier import Do_Carrier

class Command_Intake_Pickup(CommandGroup):

	def __init__(self, robot):
		CommandGroup.__init__(self, name='Command_Intake_Pickup')
		print("command group intake pickup init!!")
		# retract as soon as released maybe
		self.robot = robot
		#XXX just combined do_four_bar into the Do_Intake command since
		# they're the same subsystem
		#self.addSequential(Do_Four_Bar(robot))
		self.addParallel(Do_Intake(robot))
		self.addParallel(Do_Carrier(robot))
		#self.addSequential(Do_Four_Bar_Inside(robot))
