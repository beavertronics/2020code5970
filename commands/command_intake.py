# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Command_Intake(Command):
	def __init__(self, robot):
		Command.__init__(self, name='Command_Intake')
		# Recognize as a wpilib command
		#print("command_intake init")
		self.requires(robot.intake)
		self.requires(robot.carrier)
		self.intake = robot.intake
		self.carrier = robot.carrier
	
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
	
	#XXX Maybe don't want to stop motors when interrupted
	def interrupted(self):
		self.end()
