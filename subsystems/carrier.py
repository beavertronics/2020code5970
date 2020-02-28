# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from simple_pid import PID
import logging

class Carrier(Subsystem):
	#s = {'p':0.5, 'i':0.02, 'd':0.001, 'setpoint':0.1}
	#def __init__(self, robot, settings=s):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__("carrier")
		# Subsystem.__init__(self, "carrier")
		
		#XXX PID COMMENTED OUT FOR TESTING
		self.carrier_motor = wpilib.VictorSP(5)
		self.carrier_setpoint = 0.5
		#XXX UNTUNED
		self.pid = PID(0.2, 0, 0, setpoint=self.carrier_setpoint)
		self.pid.output_limits = (-1,1)

		#initialize carrier encoder
		#XXX DIO values and pulses_per_rev incorrect for now
		# the 6,7 below should be within the settings passed in.

		# Need to fix encoder init
		self.carrier_encoder = wpilib.Encoder(6, 7)
		pulses_per_rev = 12
		self.carrier_encoder.setDistancePerPulse(pulses_per_rev)
		#XXX not accurate
		self.setpoint_range = range(0, 1000)

	#Sets carrier motor to object's given motor speed, will be determined later
	def activate_carrier(self):
		output = self.get_pid_output()
		#output = -0.3
		#XXX changed to set instead of setSpeed
		self.carrier_motor.set(output)
		logging.info('set carrier motor speed ' + str(output))
	
	def deactivate_carrier(self):
		self.carrier_motor.set(0)

	def get_pid_output(self):
		current_rpm = self.get_encoder_rpm()
		# what is this output telling you from self.pid
		output = self.pid(current_rpm)
		return output

	def reverse_carrier(self):
		speed = self.carrier_motor.get()
		new_speed = speed * -1
		self.carrier_motor.set(new_speed)
	
	def get_encoder_rpm(self):
		angular_velocity_rpm = self.carrier_encoder.getRate()
		return angular_velocity_rpm
