# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from do_shoot import Do_Shoot
from do_stop_shoot import Do_Stop_Shoot
from do_carrier import Do_Carrier
from do_activate_feeder import Do_Activate_Feeder
from do_feeder import Do_Feeder

class Command_Shoot(CommandGroup):
	def __init__(self, robot):
		super().__init__()
#		# Recognize as a wpilib command
#		Command.__init__(self)
#		print("Doing Command_Shoot!!")
#		self.addSequential(Do_Carrier(robot))
#		#XXX I think this should be parallel so that it continues to run
#		# the flywheel when we use things like carrier and feeder. -lolly
#		self.addParallel(Do_Shoot(robot))
#		self.addParallel(Do_Feeder(robot))
#		self.addSequential(Do_Stop_Shoot(robot))
#		# Command groups don't need end functions and the like because 
#		# those functions are defined in the individual commands

		# Command.__init__(self)
		print("Doing Command_Shoot!!")
		self.addSequential(Do_Carrier(robot))
		import pdb; pdb.set_trace()
		self.addParallel(Do_Shoot(robot))
		self.addParallel(Do_Activate_Feeder(robot))
