# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Tank_Drive(Command):

	def __init__(self, robot):
		print("do_tank_drive init")
		Command.__init__(self)

		# an instance of BeaverTronicsRobot from robot.py containing its
		# instance of drivetrain
		self.robot_dt = robot.drivetrain
		self.requires(self.robot_dt)
		self.robot = robot

		self.left_joy = robot.left_joy
		self.right_joy = robot.right_joy
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.robot_dt.stop_robot()
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		# Continuously sets motor speed to joystick inputs w/ Scheduler
		self.robot_dt.set_tank_speed(self.left_joy, self.right_joy)

	def isFinished(self):
		# This is how running tank driving is prioritized
		# In other words, runs til interrupted
		return False

	def end(self):
		# Stop motors when ending command
		self.robot_dt.stop_robot()
	
	def interrupted(self):
		self.end()
