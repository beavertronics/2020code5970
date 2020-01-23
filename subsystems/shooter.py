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
		self.shooter_motor = wpilib.VictorSP(7)
		
		#setpoint = self.get_setpoint()
		#setpoint = robot.setpoint
		self.pid = PID(0.2, 0.1, 0.1, setpoint=0.2)
		self.pid.output_limits = (-1,1)

		#Initializes shooter encoder
		#XXX DIO_1 and DIO_2 are incorrect for now
		self.shooter_encoder = Shooter_Encoder(8,9)

	def shoot(self):
		''' Shoots the ball by controlling the flywheel motor '''
		#XXX Need to get pid_output 
		output = self.get_pid_output()
		self.shooter_motor.setSpeed(output)

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



