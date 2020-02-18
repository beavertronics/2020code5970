# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive

# Subsidiaries to subsystems; sub-subs
from left_motors import Left_Motors
from right_motors import Right_Motors

# Commands
from sys import path
path.append('../commands')
from do_tank_drive import Do_Tank_Drive

import math
import time


class Drivetrain(Subsystem):

	def __init__(self, robot):
		# Super from subsystem allows scheduler class to understand things like
		# interupt and execute etc...
		#print("-------Drivetrain--------")
		
		#print("---------------")
		super().__init__("drivetrain")
		# Subsystem.__init__(self, "drivetrain")
	
		# Motors
		left_motors_instance = Left_Motors()
		right_motors_instance = Right_Motors()
		self.left_motors = left_motors_instance.left_motor_group
		self.right_motors = right_motors_instance.right_motor_group

		# Encoders
		self.left_drive_encoder = wpilib.Encoder(2,3)#DIO Ports??
		self.right_drive_encoder = wpilib.Encoder(4,5)#DIO Ports??

		# Instantiate robot
		self.robot_instance = robot
	
		# Tank Drive Drivetrain
		self.drive = self.set_drivetrain_type(DifferentialDrive, 
			self.left_motors, self.right_motors)

		self.drive.setSafetyEnabled(False)

	def initDefaultCommand(self):
		self.setDefaultCommand(Do_Tank_Drive(self.robot_instance))

	# Sets driving mode to tank drive, should be periodically called
	def set_drivetrain_type(self, drivetrain_type, left_motors, right_motors):
		# DifferentialDrive for tank
		drive = drivetrain_type(left_motors, right_motors)
		return drive

	# Sets motor speeds to joystick inputs
	def set_tank_speed(self, left_joy, right_joy, drive=DifferentialDrive):
		left_speed = left_joy.getY()
		right_speed = right_joy.getY() 
		self.drive.tankDrive(left_speed, right_speed)
		#drive.feed()

	#def stop_robot(self, drive=DifferentialDrive):
	def stop_robot(self):
		self.drive.tankDrive(0.0, 0.0)

	#def bad_auto_drive(self, drive=DifferentialDrive):
#	def bad_auto_drive(self):
#		# We start x feet away from the tower if directly in front
#		# Therefore we can use the encoder to figure out when we are close
#		# enough. Or we could just run into it and shoot
#
#		# In seconds
#		total_run_time = time.time() + 4
#		# Runs motors straight forward for four seconds at half speed
#		while time.time() < total_run_time:
#			self.drive.tankDrive(0.5, 0.5)
	
#	def reset_encoder(self):
#		self.right_encoder.reset()

	

		
		

