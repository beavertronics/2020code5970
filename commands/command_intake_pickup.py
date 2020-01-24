# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from do_intake import Do_Intake
from do_four_bar import Do_Four_Bar

class Command_Intake_Pickup(CommandGroup):

    def __init__(self, robot):

        super().__init__()

    def execute(self):
        print("command group intake pickup initialized")
        self.addSequential(Do_Four_Bar)
        # intake delay command has not yet been created
        # self.addSequential(Do_Intake_Delay, 0.2)
        self.addSequential(Do_Intake)
