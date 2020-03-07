# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from simple_pid import PID
import logging
import math

class Carrier(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__("carrier")
		
		# CARRIER is 4
		self.carrier_motor = wpilib.VictorSP(4)
		#XXX watch the negative
		self.carrier_setpoint = -0.4
		#XXX UNTUNED
		self.pid = PID(0.4, 0, 0, setpoint=self.carrier_setpoint)
		self.pid.output_limits = (-1,1)

		#initialize carrier encoder
		self.carrier_encoder = wpilib.Encoder(4, 5)
		self.carrier_encoder.reset()
		# If setting dist per pulse as radians per pulse
		# (1 encoder_rev / 12 pulses) 
		# (1 wheel rev / 1 encoder_rev) ( 2 pi / 1 wheel_rev) = pi / 6
		radians_per_pulse = math.pi / 6
		self.carrier_encoder.setDistancePerPulse(radians_per_pulse)

		#XXX not accurate, CANT INTERPRET FLOAT AS INT
		#self.setpoint_range = range(.35, .45)
		self.setpoint_range = range(-1, 1)

	#Sets carrier motor to object's given motor speed, will be determined later
	def activate_carrier(self):
		output = self.get_pid_output()
		self.carrier_motor.set(output)
		#logging.info('set carrier motor speed ' + str(output))
	
	def deactivate_carrier(self):
		self.carrier_motor.set(0)

	def reverse_carrier(self):
		speed = self.carrier_motor.get()
		new_speed = speed * -1
		self.carrier_motor.set(new_speed)

	def convert_rpm_to_pwm(self, rpm):
		# 18,730 rpm for 12V applied to a 775 pro motor
		# vexrobotics.com/775pro.html#Other_Info
		pwm = rpm / 18730
		return pwm
	
	def get_encoder_rpm(self):
		angular_vel = self.carrier_encoder.getRate()
		rpm = angular_vel / (2*math.pi) * 60
		return rpm

	def get_pid_output(self):
		current_rpm = self.get_encoder_rpm()
		print('CARRIER RPM: ' + str(current_rpm))
		pwm = self.convert_rpm_to_pwm(current_rpm)
		output = self.pid(pwm)
		return output

