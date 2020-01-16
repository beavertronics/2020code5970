# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from simple_pid import PID
from encoder import encoder.ang_velocity

class Shooter(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self):
		'''
		Command Dependencies:

		'''
		super().__init__()
		# Assumes four PWM ports for motors
		self.shooter_motor = wpilib.VictorSP(5)

	def shoot(self):
		''' Shoots the ball by controlling the flywheel motor '''
		#XXX Need to get pid_output 
		pid_output = self.get_velocity()
		self.shooter_motor.set(pid_output)

	# Private functions
	def get_motor_speed(self):
		# get current speed from encoders
		pass
	
	def get_pid_velocity(self):
		# Gets the output velocity from the pid loop
		pid = PID(0.2, 0.1, 0.05, setpoint=10)		

		while True:
			control = pid(v)
		pass

	def calc_error(self):
		actual_v = encoder.velocity
		error = desired_v - actual_v

	def get_velocity(self):
		# Converts the motor speed to velocity which can be used for error calcs
		pass

