# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../subsystems')
from unittest import mock
import unittest
from shifters import Shifters
from parametrized import ParametrizedTestCase

class Test_Shifters(ParametrizedTestCase):

	# This method is run once before running ALL tests
	@classmethod
	def setUpClass(cls):
		print('setUpClass()')

	# This method is run once before running EACH test
	def setUp(self):
		#self.shift = Shifters()
		print('setUp()')

	def test_param_on(self):
		print('test_param_on()')
		self.param.shifters_on()
		l_status = self.param.shifter_solenoid_left.get()
		r_status = self.param.shifter_solenoid_right.get()
		assert l_status == True
		assert r_status == True

	def test_param_off(self):
		print('test_shifters_off()')
		self.param.shifters_off()
		l_status = self.param.shifter_solenoid_left.get()
		r_status = self.param.shifter_solenoid_right.get()
		assert l_status == False
		assert r_status == False

	def tearDown(self):
		print('setUp()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
