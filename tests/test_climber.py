# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
import wpilib
from unittest import mock
import unittest
from climber import Climber
from parametrized import ParametrizedTestCase

class Test_Climber(ParametrizedTestCase):
	
	# This method is run once before running ALL tests
	@classmethod
	def setUpClass(cls):
		print('setUpClass()')
	
	# This method is run once before running EACH test
	def setUp(self):
		print('setUp()')

	def test_big_actuate(self):
		print('test_big_actuate()')
		self.param.big_actuate()
		solenoid = self.param.biggum.get()
		assert(solenoid == True)

	def test_big_unactuate(self):
		print('test_big_unactuate()')
		self.param.big_unactuate()
		solenoid = self.param.biggum.get()
		assert(solenoid == False)

	def test_little_actuate(self):
		print('test_little_actuate()')
		self.param.little_actuate()
		solenoid = self.param.littlum.get()
		assert(solenoid == True)
		
	def test_little_unactuate(self):
		print('test_little_unactuate()')
		self.param.little_unactuate()
		solenoid = self.param.littlum.get()
		assert(solenoid == False)

	def test_reverse_solenoid(self):
		print('test_reverse_solenoid')
		# Test the biggum solenoid
		starting_biggum = self.param.biggum.get()
		self.param.reverse_solenoid(self.param.biggum)
		supposed_biggum = not(starting_biggum)
		actual_biggum = self.param.biggum.get()
		assert(supposed_biggum == actual_biggum)
		
		# Test the littlum solenoid
		starting_littlum = self.param.littlum.get()
		self.param.reverse_solenoid(self.param.littlum)
		supposed_littlum = not(starting_littlum)
		actual_littlum = self.param.littlum.get()
		assert(supposed_littlum == actual_littlum)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
