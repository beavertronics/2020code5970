# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem
from carrier_encoder import Carrier_Encoder
from simple_pid import PID

class Carrier(Subsystem):
	#s = {'p':0.5, 'i':0.02, 'd':0.001, 'setpoint':0.1}
	#def __init__(self, robot, settings=s):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		super().__init__()
		self.carrier_motor = wpilib.VictorSP(8)
		self.pid = PID(0.5, 0.02, 0.001, 0.1)
		#self.carrier_setpoint = s['setpoint']  
		#self.pid = PID(s['p'], s['i'], s['d'], setpoint=self.carrier_setpoint)
		# self.pid.output_limits = (-1,1)

		#initialize carrier encoder
		#XXX DIO values incorrect for now
		# the 6,7 below should be within the settings passed in.  Also,
		# Carrier_Encoder class should be passed in and mocked in tests.
		self.carrier_encoder = Carrier_Encoder(6,7)

	#Sets carrier motor to object's given motor speed, will be determined later
	def activate_carrier(self):
		output = self.get_pid_output()
		# why setSpeed() instead of set()
		self.carrier_motor.set(output)
	
	def deactivate_carrier(self):
		self.carrier_motor.set(0)

	def get_pid_output(self):
		current_rpm = self.carrier_encoder.get_encoder_rpm()
		# what is this output telling you from self.pid
		output = self.pid(current_rpm)
		return output

	def reverse_carrier(self):
		speed = self.carrier_motor.get()
		new_speed = speed * -1
		self.carrier_motor.set(new_speed)
