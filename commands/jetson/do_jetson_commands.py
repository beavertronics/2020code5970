# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Jetson_Commands(Command):
    ''' This will send instructions for what the Jetson should start processing.
    The Jetson should eventually send back motor speeds based on the vision
    processing.'''

    def __init__(self, robot):
        print("Do_Jetson_Commands init!!")
        Command.__init__(robot)

    def execute(self):
        # Call can.sh on Jetson
        pass

    def isFinished(self):
        pass

    def end(self):
        pass

    def interrupted(self):
        pass
