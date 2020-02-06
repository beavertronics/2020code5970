# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock
import unittest
from winch import Winch
from parametrized import ParametrizedTestCase

class Test_Winch(ParametrizedTestCase):
	
	# This method is run once before running ALL tests
	@classmethod
	def setUpClass(cls):
		print('setUpClass()')
	
	# This method is run once before running EACH test
	def setUp(self):
		print('setUp()')

	def test_roll_up(self):
		print('test_roll_up()')
		self.param.roll_up()
		motor = self.param.winch_motor.get()
		assert(motor == 1)

	def test_stop_motor(self):
		print('test_stop_motor()')
		self.param.stop_motor()
		motor = self.param.winch_motor.get()
		assert(motor == 0)

	def test_unroll(self):
		print('test_unroll()')
		self.param.unroll()
		motor = self.param.winch_motor.get()
		assert(motor == -1)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
