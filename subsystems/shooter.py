# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib from wpilib.command 
import Subsystem
from simple_pid import PID
from encoder import encoder.ang_velocity

class Shooter(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self, robot):
		'''
		Command Dependencies:

		'''
		super().__init__()
		# Assumes four PWM ports for motors
		self.shooter_motor = wpilib.VictorSP(5)
		
		#Values currently arbitrary
		#setpoint = self.get_setpoint()
		setpoint = robot.setpoint
		self.pid = PID(0.2, 0.1, 0.05, setpoint=setpoint)
		pid.output_limits = (0,10)

	def shoot(self):
		''' Shoots the ball by controlling the flywheel motor '''
		#XXX Need to get pid_output 
		output = self.get_pid_output()
		self.shooter_motor.set(output)

	def get_rpm(self):
		rpm = encoder.ang_velocity * k
		return rpm

	def get_pid_output(self):
		output = self.pid(self.get_rpm())
		return output

#	def get_setpoint(self, setpoint):
#		'''Setpoint value not changing mayhaps (archaic)'''
#		#XXX maybe have user input from GUI or something
#		# maybe also pass in as arg
#		#Fake val
#		return setpoint



