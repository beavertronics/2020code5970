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
		#print("drivetrain init! no seg fault please")

		self.robot = robot
		self.lm_inst = Left_Motors().left_motor_group
		self.rm_inst = Right_Motors().right_motor_group
		self.drive = DifferentialDrive(self.lm_inst, self.rm_inst)
		#self.SetSafetyEnabled(False)
		#XXX encoder DIO inputs and pulses_per_rev are currently incorrect
		pulses_per_rev = 12
		# gear_reduction = 1:1
		self.right_encoder = wpilib.Encoder(0, 1)
		self.right_encoder.setDistancePerPulse(pulses_per_rev)
		self.left_encoder = wpilib.Encoder(2, 3)	
		self.left_encoder.setDistancePerPulse(pulses_per_rev)
		#self.gyro = wpilib.interfaces.Gyro()
		#XXX override calibrate?
		#self.gyro.calibrate()

		# init with gyroAngle and initialPose
		#gyro_angle = self.gyro.getAngle()
		#XXX different possible starting positions, manual input? vision?
		#initial_pose = 0
		#XXX missing the params for DifferentialDriveOdometry()
		#self.drive_odometry = DifferentialDriveOdometry()
		
	def initDefaultCommand(self):
		self.setDefaultCommand(Do_Tank_Drive(self.robot))

	def set_tank_speed(self, left_joy, right_joy):
		left_speed = left_joy.getY()
		right_speed = right_joy.getY()
		self.drive.tankDrive(left_speed, right_speed)

	def stop_robot(self):
		self.drive.tankDrive(0,0)

	def get_robot_position(self):
		right_encoder_distance = self.right_encoder.getDistance()
		left_encoder_distance = self.left_encoder.getDistance()
		gyro_angle = self.gyro.getAngle()
		robot_position = self.drive_odometry.update(gyro_angle,
				left_encoder_distance, right_encoder_distance)
		return(robot_position)

