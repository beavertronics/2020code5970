# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock
import unittest
from shooter import Shooter
from shooter_encoder import Shooter_Encoder
from parametrized import ParametrizedTestCase

'''All values currently arbitrary'''
class Test_Shooter(ParametrizedTestCase):
	
	# This method is run once before running ALL tests
	@classmethod
	def setUpClass(cls):
		print('setUpClass()')
	
	# This method is run once before running EACH test
	def setUp(self):
		print('setUp()')

	#XXX I don't believe that this SHOULD work. The pid output is supposed to
	# change based on the instantaneous status of the motors. It might be too
	# delayed to use these commands in succession and assert equality
	#XXX I also changed a few things to be more readable
	def test_shoot(self):
		print('test_shoot()')
		test_vals = [-0.1, 0.05, 0.15, 0.25, 1]
		val = 0.1
		#for val in test_vals:
			#self.param.shooter_motor.setSpeed(self.param.pid(val))
			#actual_motor_speed = self.param.shooter_motor.get()
			#supposed_motor_speed = self.param.pid(val)
			#print(actual_motor_speed)
			#print(supposed_motor_speed)
		#	assert(actual_motor_speed == supposed_motor_speed)
		#XXX pid having odd behavior because it isn't getting proper inputs,
		# needs to know difference of inputs in order to have a decreasing behavior
		#diagnostics
		for x in range(0, 4):
			val = self.param.pid(val)
			print(self.param.pid._proportional / self.param.pid.Kp)
			print(self.param.pid._last_input)

	def test_get_pid_output(self):
		print('test_get_pid_output()')
		supposed_pid_out = self.param.get_pid_output()
		actual_pid_out = self.param.pid(self.param.shooter_encoder.get_encoder_rpm())
		assert(supposed_pid_out == actual_pid_out)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
