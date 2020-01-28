# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock
import unittest
from intake import Intake
from parametrized import ParametrizedTestCase

class Test_Intake(ParametrizedTestCase):
	
	# This method is run once before running ALL tests
	@classmethod
	def setUpClass(cls):
		print('setUpClass()')
	
	# This method is run once before running EACH test
	def setUp(self):
		print('setUp()')

	def test_fourbar_eject(self):
		print('test_fourbar_eject()')
		self.param.fourbar_eject()
		assert(self.param.fourbar.get() == True)
	
	def test_fourbar_inject(self):
		print('test_fourbar_inject()')
		self.param.fourbar_inject()
		assert(self.param.fourbar.get() == False)

	#Gets pwm_val from intake.py
	def test_activate_intake(self):
		pwm_val = 0.5
		self.param.intake_motor.set(pwm_val)
		motor_val = self.param.intake_motor.get()
		assert(motor_val == pwm_val)
	
	def test_backwards_intake(self):
		pwm_val = 0.5
		new_pwm_val = -1 * pwm_val
		self.param.intake_motor.set(new_pwm_val)
		motor_val = self.param.intake_motor.get()
		assert(motor_val == new_pwm_val)
		
	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
