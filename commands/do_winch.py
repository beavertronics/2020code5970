# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Winch(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("Winch init!!")
		#super().__init__()
		self.requires(robot.winch)
		self.winch = robot.winch
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		print("Do_Winch execute!!")
		# Continuously sets motor speed to joystick inputs w/ Scheduler
		self.winch.roll_up()

	def isFinished(self):
		return True

	def end(self):
		# Stop motors when ending command
		#XXX This may cause issues... ex if holding button down, will it
		# roll up a little then stop then roll up a little or will it just
		# run the execute func until the button is released?
		self.winch.stop_motor()
	
	def interrupted(self):
		self.end()
