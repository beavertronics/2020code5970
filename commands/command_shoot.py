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
		CommandGroup.__init__(self, name='Command_Shoot')
		print("Command_Shoot init!!")

#		#XXX I think this should be parallel so that it continues to run
#		# the flywheel when we use things like carrier and feeder. -lolly
		#self.addSequential(Do_Carrier(robot))
		self.addParallel(Do_Shoot(robot))
		#self.addParallel(Do_Activate_Feeder(robot))
