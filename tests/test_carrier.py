# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock
import unittest
from carrier import Carrier
from parametrized import ParametrizedTestCase

class Test_Carrier(ParametrizedTestCase):
	# Values arbitary and taken from carrier.py
	# This method is run once before running ALL tests
	@classmethod
	def setUpClass(cls):
		print('setUpClass()')
	
	# This method is run once before running EACH test
	def setUp(self):
		print('setUp()')

	def test_activate_carrier(self):
		print('test_activate_carrier()')
		self.param.activate_carrier()
		supposed_speed = self.param.motor_speed = 0.3
		actual_speed = self.param.carrier_motor.get()
		assert(supposed_speed == actual_speed)

	def test_deactivate_carrier(self):
		print('test_deactivate_carrier()')
		self.param.deactivate_carrier()
		supposed_speed = 0
		actual_speed = self.param.carrier_motor.get()
		assert(supposed_speed == actual_speed)

	def test_reverse_carrier(self):
		print('test_reverse_carrier()')
		before_speed = self.param.carrier_motor.get()
		self.param.reverse_carrier()
		supposed_speed = before_speed * -1
		actual_speed = self.param.carrier_motor.get()
		assert(supposed_speed == actual_speed)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
