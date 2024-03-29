# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from simple_pid import PID
import logging
import math

class Shooter(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__("shooter")
		self.robot = robot
		# Correct shoooter pwm
		#pwm 0 not functional
		#pwm 1 motor whirs, no motion
		#pwm 2 is right drivetrain. not functional 
		#pwm 3 is left drivetrain. not functional
		#pwm 4 is intake. good
		#pwm 5 is carrier. good
		#pwm 6 is left drivetrain. good 
		#pwm 7 is shooter. good
		#pwm 8 not functional
		#pwm 9 is right drivetrain. good
		#need to replace nonfunctional motor controllers. just go with victor sps that we know work (test with motor before mounting)
		self.shooter_motor = wpilib.VictorSP(7)
		#XXX UNTUNED SETPOINT 1 and PID(0.85, 0, 0)
		#XXX UNTUNED SETPOINT 1 and PID(0.85, 0, 0.05)

		self.setpoint = 0.85 
		self.pid = PID(0.85, 0, 0, 
			setpoint=self.setpoint, proportional_on_measurement=False)
		self.pid.output_limits = (-1,1)

		#Initializes shooter encoder
		self.shooter_encoder = wpilib.Encoder(0, 1)
		self.shooter_encoder.reset()
		# If setting dist per pulse as radians per pulse
		# (1 encoder_rev / 12 pulses) 
		# (1 wheel rev / 1 encoder_rev) ( 2 pi / 1 wheel_rev) = pi / 6
		radians_per_pulse = math.pi / 6
		self.shooter_encoder.setDistancePerPulse(radians_per_pulse)
		#XXX not accurate needs testing
		# Should be roughly the same as the setpoint voltage
		self.setpoint_range = [.8, .9]

	def shoot(self):
		''' Shoots the ball by controlling the flywheel motor '''
		output = self.get_pid_output()
		self.shooter_motor.set(output)
		print('output: ' + str(output))
		print('ACTUAL SPEED: ' + str(self.shooter_motor.get()))
		#logging.info('set shooter motor speed ' + str(output))

	def stupid_shoot(self, val):
		self.shooter_motor.set(val)
		
	def stop_shoot(self):
		self.shooter_motor.set(0)

	def get_encoder_rpm(self):
		# angular_vel is returned in rad/sec
		angular_vel = self.shooter_encoder.getRate()
		rpm = angular_vel / (2*math.pi) * 60
		return rpm

	def convert_rpm_to_pwm(self, rpm):
		# 18,730 rpm for 12V applied to a 775 pro motor
		# vexrobotics.com/775pro.html#Other_Info
		pwm = rpm / 18730
		return pwm

	#XXX pid gets pwm input and should do pwm output
	# pid must not be working
	def get_pid_output(self):
		current_rpm = self.get_encoder_rpm()
		print('ENCODER RPM: ' + str(current_rpm))
		print('ENCODER COUNT: ' + str(self.shooter_encoder.get()))
		pwm = self.convert_rpm_to_pwm(current_rpm)
		output = self.pid(pwm)
		return output

