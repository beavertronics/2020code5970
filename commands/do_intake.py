# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Intake(Command):

    def __init__(self, robot):
		print("do_intake init")
        Command.__init__(self)
        
        self.intake = robot.intake

    def initialize(self):
        return None

    def execute(self):
        self.intake.activate_intake()

    def isFinished(self):
        return True

    def end(self):
        return None
