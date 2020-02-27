# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Cancel_Current_Com(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("do_cancel_current_com init!!")
		Command.__init__(self)
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		# Continuously sets motor speed to joystick inputs w/ Scheduler
		self.robot_dt.set_tank_speed(
			self.left_joy, self.right_joy, self.robot_dt.drive)

	def isFinished(self):
		# This is how running tank driving is prioritized
		# In other words, runs til interrupted
		return False

	def end(self):
		# Stop motors when ending command
		self.robot_dt.stop_robot(self.robot_dt.drive)
	
	def interrupted(self):
		self.end()
