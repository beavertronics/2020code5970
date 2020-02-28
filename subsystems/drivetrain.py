# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive
#from wpilib.kinematics import DifferentialDriveOdometry
from left_motors import Left_Motors
from right_motors import Right_Motors

import sys
sys.path.append('../commands')
from do_tank_drive import Do_Tank_Drive

class Drivetrain(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:
			Do_Tank_Drive()

		'''
		super().__init__("drivetrain")

		self.robot = robot
		self.lm_inst = Left_Motors().left_motor_group
		self.rm_inst = Right_Motors().right_motor_group
		self.drive = DifferentialDrive(self.lm_inst, self.rm_inst)
		#self.SetSafetyEnabled(False)
		#XXX encoder DIO inputs and pulses_per_rev are currently incorrect
		pulses_per_rev = 12
		# gear_reduction = 1:1
		#XXX .get() function returning 0 for the encoders even when wheels
		# are turning
		self.right_encoder = wpilib.Encoder(0, 1)
		self.right_encoder.setDistancePerPulse(pulses_per_rev)
		self.left_encoder = wpilib.Encoder(2, 3)	
		self.left_encoder.setDistancePerPulse(pulses_per_rev)
		self.gear_ratio = 12.75

		self.gyro = wpilib.ADXRS450_Gyro()
		# This MUST occur while this doesn't move
		self.gyro.calibrate()
		# init with gyroAngle and initialPose
		gyro_angle = self.gyro.getAngle()
		# initial_pose should be in form of (x position, y position, rotation)
		initial_pose = (0, 0, 0)
		#XXX missing the params for DifferentialDriveOdometry()
		#self.drive_odometry = wpilib.kinematics.DifferentialDriveOdometry(
				#gyro_angle, initial_pose)
		
	def initDefaultCommand(self):
		self.setDefaultCommand(Do_Tank_Drive(self.robot))

	def set_tank_speed(self, left_joy, right_joy):
		left_speed = left_joy.getY()
		right_speed = right_joy.getY()
		self.drive.tankDrive(left_speed, right_speed)
		print(self.left_encoder.get())
		print(self.right_encoder.get())

	def stop_robot(self):
		self.drive.tankDrive(0,0)

	def get_robot_position(self):
		right_encoder_distance = self.right_encoder.getDistance()
		left_encoder_distance = self.left_encoder.getDistance()
		gyro_angle = self.gyro.getAngle()
		robot_position = self.drive_odometry.update(gyro_angle,
				left_encoder_distance, right_encoder_distance)
		return(robot_position)

	#XXX kinda just guessing about this orientation for now... may change
	''' In our code, the field will be represented as a plane with y = 0 
	representing the wall of our alliance's drivestations; x = 0 represents 
	the left wall when you are facing the field from the perspective of our
	alliance's drivestation. Basically, picture you are driving the robot on
	the field with left being the negative x direction and forward (away 
	from you) being the positve y direction.'''
	def which_path(self, start_position):
		''' 
		Left, middle, and right will be predefined distances from the wall.
		This approach does not require vision to orient the robot, but does
		require precise positioning and 
		'''

		if start_position == 'left':
			self.a_path_follow()
		if start_position == 'middle':
			self.b_path_follow()
		if start_position == 'right':
			self.c_path_follow()

	def a_path_follow(self):
		pass
	def b_path_follow(self):
		pass
	def c_path_follow(self):
		pass


