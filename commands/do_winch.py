# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Winch(Command):

	def __init__(self, robot):
		Command.__init__(self)
		print("do_winch init!!")
		self.requires(robot.winch)
		self.winch = robot.winch
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		# Continuously sets motor speed to joystick inputs w/ Scheduler
		self.winch.roll_up()

	def isFinished(self):
		pass

	def end(self):
		# Stop motors when ending command
		self.winch.stop_motor()
	
	def interrupted(self):
		self.end()
