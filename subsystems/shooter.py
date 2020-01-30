# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from simple_pid import PID
from shooter_encoder import Shooter_Encoder
class Shooter(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__()
		# Assumes four PWM ports for motors
		#XXX shooter is on wrong PWM for now
		self.shooter_motor = wpilib.VictorSP(4)
		
		#setpoint = self.get_setpoint()
		#setpoint = robot.setpoint
		self.setpoint = 0.3
		self.pid = PID(0.5, 0.02, 0.001, setpoint=self.setpoint)
		self.pid.output_limits = (-1,1)

		#Initializes shooter encoder
		#XXX DIO_1 and DIO_2 are incorrect for now
		self.shooter_encoder = Shooter_Encoder(8,9)

	def shoot(self):
		''' Shoots the ball by controlling the flywheel motor '''
		#XXX Need to get pid_output 
		output = self.get_pid_output()
		self.shooter_motor.setSpeed(output)
		
	def stop_shoot(self):
		self.shooter_motor.setSpeed(0)

	def get_pid_output(self):
		current_rpm = self.shooter_encoder.get_encoder_rpm()
		output = self.pid(current_rpm)
		return output

#XXX Not sure if a getter for setpoint is necessary
#	def get_setpoint(self, setpoint):
#		'''Setpoint value probably not changing'''
#		#XXX maybe have user input from GUI or something
#		# maybe also pass in as arg
#		#Fake val
#		return setpoint



