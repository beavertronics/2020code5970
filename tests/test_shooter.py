# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock
import unittest
from shooter import Shooter
#from shooter_encoder import encoder.ang_velocity
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
		#XXX why is the line below there?
		#self.param.shoot()
		actual_motor_speed = self.param.shooter_motor.get()
		supposed_motor_speed = self.param.shooter_motor.setSpeed(
			self.param.get_pid_output())
		assert(actual_motor_speed == supposed_motor_speed)
	
	def test_get_rpm(self):
		print('test_get_rpm()')
		supposed_rpm = self.param.get_rpm()
		actual_rpm = 5 * 4
		#actual_rpm == angular velocity * arbitrary constant
		assert(supposed_rpm == actual_rpm)

	def test_get_pid_output(self):
		print('test_get_pid_output()')
		supposed_pid_out = self.param.get_pid_output()
		actual_pid_out = self.param.pid(self.param.get_rpm())
		assert(supposed_pid_out == actual_pid_out)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
