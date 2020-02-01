# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock
import unittest
from feeder import Feeder
from parametrized import ParametrizedTestCase

class Test_Feeder(ParametrizedTestCase):
	
	# This method is run once before running ALL tests
	@classmethod
	def setUpClass(cls):
		print('setUpClass()')
	
	# This method is run once before running EACH test
	def setUp(self):
		print('setUp()')

	def test_activate_feeder(self):
		print('test_activate_feeder()')
		self.param.activate_feeder()
		supposed_speed = self.param.motor_speed
		actual_speed = self.param.feeder_motor.get()
		assert(supposed_speed == actual_speed)

	def test_deactivate_feeder(self):
		print('test_deactivate_feeder()')
		self.param.deactivate_feeder()
		supposed_speed = 0
		actual_speed = self.param.feeder_motor.get()
		assert(supposed_speed == actual_speed)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
