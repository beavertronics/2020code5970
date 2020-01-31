# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Shoot(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print(str(robot) + "!!")
		super().__init__()
		self.requires(robot.shooter)
		self.shooter = robot.shooter
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.shooter.stop_shoot()	
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		print("Shoot executed!!")
		self.shooter.shoot()

	def isFinished(self):
		# Once the the motor speed has reached the goal rpm, it can stop
		#XXX BELOW SHOULD GO IN CONDITIONAL COMMAND FOR FEEDER ACTIVATION
		current_rpm = self.shooter.shooter_encoder.get_encoder_rpm()
		goal_rpm = self.shooter.setpoint
		
		if(current_rpm == goal_rpm):
			finished = True
		else:
			finished = False

		return finished

	def end(self):
		pass

	def interrupted(self):
		self.end
