# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
import time

class Do_Intake(Command):
    def __init__(self, robot):
	print("command_intake init!!")
	Command.__init__(self)
	self.requires(robot.intake)
	self.intake = robot.intake
	
    def initialize(self):
	"""Called just before this Command runs the first time"""
	pass
	#self.old_time = time.time_ns()
	#self.intake.fourbar_eject()
	
    def execute(self):
	"""Called iteratively by Scheduler"""
	self.stupid_intake(0.4)	

    def isFinished(self):
	pass

    def end(self):
#	self.intake.fourbar_inject()
	self.intake.deactivate_intake()
	
    def interrupted(self):
	self.end()
