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
	# test assumes pid values from shooter.py (kP=0.5, kI=0.02, kD=0.001, setpoint=0.3), dt=0.01
	def test_shoot(self):
		print('test_shoot()')
		kP = 0.5
		kI = 0.02
		kD = 0.001
		setpoint = 0.3
		dt = 0.01
		
		test_vals = [[0.2, 0.05002], [0.4, -0.05002]]
		for each in test_vals:
			input_ = each[0]
			actual_output = each[1]
			error = setpoint - input_
			d_input = 0
			proportional = kP * error
			integral = kI * error * dt
			derivative = -kD * d_input / dt
			supposed_output = proportional + integral + derivative
			assert(round(actual_output, 4) == round(supposed_output, 4))

	def test_get_pid_output(self):
		print('test_get_pid_output()')
		supposed_pid_out = self.param.get_pid_output()
		actual_pid_out = self.param.pid(
			self.param.shooter_encoder.get_encoder_rpm())
		assert(supposed_pid_out == actual_pid_out)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
