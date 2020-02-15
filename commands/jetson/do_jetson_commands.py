# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Jetson_Commands(Command):
^I''' This will send instructions for what the Jetson should start processing.
^IThe Jetson should eventually send back motor speeds based on the vision
^Iprocessing.'''

^Idef __init__(self, robot):
^I^Iprint("Do_Jetson_Commands init!!")
^I^ICommand.__init__(self)

^Idef execute(self):
^I^I# Call can.sh on Jetson
^I^Ipass

^Idef isFinished(self):
^I^Ipass

^Idef end(self):
^I^Ipass

^Idef interrupted(self):
^I^Ipass
