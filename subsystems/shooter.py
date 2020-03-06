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
		self.shooter_motor = wpilib.VictorSP(4)
		#XXX UNTUNED SETPOINT 1 and PID(0.85, 0, 0)
		#XXX UNTUNED SETPOINT 1 and PID(0.85, 0, 0.05)

		self.setpoint = 0.85 
		self.pid = PID(0.85, 0, 0, 
			setpoint=self.setpoint, proportional_on_measurement=False)
		self.pid.output_limits = (-1,1)

		#Initializes shooter encoder
		#XXX DIO_1 and DIO_2 and pulses_per_rev are incorrect for now
		self.shooter_encoder = wpilib.Encoder(0, 1)
		self.shooter_encoder.reset()
		# If setting dist per pulse as radians per pulse
		# (1 encoder_rev / 12 pulses) 
		# (1 wheel rev / 1 encoder_rev) ( 2 pi / 1 wheel_rev) = pi / 6
		radians_per_pulse = math.pi / 6
		self.shooter_encoder.setDistancePerPulse(radians_per_pulse)
		#XXX not accurate
		self.setpoint_range = range(0, 1000)

	def shoot(self):
		''' Shoots the ball by controlling the flywheel motor '''
		output = self.get_pid_output()
		self.shooter_motor.set(output)
		print('output: ' + str(output))
		print('ACTUAL SPEED: ' + str(self.shooter_motor.get()))
		#error = 1 - self.shooter_motor.get()
		#print('ERROR: ' + str(error))
		#logging.info('set shooter motor speed ' + str(output))
		
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

	#XXX we think we should input pwm to get a pwm output from pid
	def get_pid_output(self):
		current_rpm = self.get_encoder_rpm()
		print('ENCODER RPM: ' + str(current_rpm))
		print('ENCODER COUNT: ' + str(self.shooter_encoder.get()))
		pwm = self.convert_rpm_to_pwm(current_rpm)
		output = self.pid(pwm)
		return output

