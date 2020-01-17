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

	def test_shoot(self):
		print('test_shoot()')
		self.param.shoot()
		motor_speed = self.param.shooter_motor.get()
		assert  motor_speed == self.param.shooter_motor.setSpeed(
				self.param.get_pid_output())
	
	def test_get_rpm(self):
		print('test_get_rpm()')
		rpm = self.param.get_rpm()
		# rpm == angular velocity * arbitrary constant
		assert rpm == 5 * 4

	def test_get_pid_output(self):
		print('test_get_pid_output()')
		output = self.param.get_pid_output()
		assert output == self.param.pid(self.param.get_rpm())

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
