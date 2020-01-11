# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../subsystems')
from unittest import mock
import unittest
from shifters import Shifters

class Test_Shifters(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setUpClass()')

	def setUp(self):
		self.shift = Shifters()
		print('setUp()')

	def test_shifters_on(self):
		print('test_shifters_on()')
		self.shift.shifters_on()
		l_status = self.shift.shifter_solenoid_left.get()
		r_status = self.shift.shifter_solenoid_right.get()
		assert l_status == True
		assert r_status == True

	def test_shifters_off(self):
		print('test_shifters_off()')
		self.shift.shifters_off()
		l_status = self.shift.shifter_solenoid_left.get()
		r_status = self.shift.shifter_solenoid_right.get()
		assert l_status == False
		assert r_status == False

	def tearDown(self):
		print('setUp()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
