# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from do_intake import Do_Intake
from do_four_bar import Do_Four_Bar
from do_four_bar_inside import Do_Four_Bar_Inside
from do_intake_delay import Do_Intake_Delay

class Command_Intake_Pickup(CommandGroup):

    def __init__(self, robot):

        super().__init__()

    def execute(self):
        print("command group intake pickup initialized")
        self.addSequential(Do_Four_Bar)
        self.addSequential(Do_Intake_Delay, 0.2)
        self.addSequential(Do_Intake)

	def isFinished(self):
		return True

	def end(self):
		# stop rollers when ending command
		self.addSequential(Do_Intake.end())
		self.addSequential(Do_Four_Bar_Inside)
	
	def interrupted(self):
		self.end()
