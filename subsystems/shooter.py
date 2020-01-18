# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from simple_pid import PID
#from shooter_encoder import encoder.ang_velocity
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
		self.pid = PID(0.2, 0.1, 0.05, setpoint=5)
		self.pid.output_limits = (0,10)

	def shoot(self):
		''' Shoots the ball by controlling the flywheel motor '''
		#XXX Need to get pid_output 
		output = self.get_pid_output()
		self.shooter_motor.setSpeed(output)

	def get_rpm(self):
		# rpm = enconder output * arbitrary constant
		rpm = 5 * 4
		return rpm

	def get_pid_output(self):
		output = self.pid(self.get_rpm())
		return output

#XXX Not sure if a getter for setpoint is necessary
#	def get_setpoint(self, setpoint):
#		'''Setpoint value probably not changing'''
#		#XXX maybe have user input from GUI or something
#		# maybe also pass in as arg
#		#Fake val
#		return setpoint



