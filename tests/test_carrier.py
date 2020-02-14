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
		#XXX need to mock robot and make new instance of carrier so that
		# pid args for test can be passed in below
		# XXX Carrier needs a robot instance.  This is mocked.  Then
		#     we tell the mock what methods it must support.  These are
		#	  those calls to robot methods in carrier.py. I didn't see any
		#     yet.
		#self.carrier = Carrier(robot_mock, pid_param_dict)
		self.kP = 0.5
		self.kI = 0.02
		self.kD = 0.001
		self.setpoint = 0.3
		self.dt = 0.01

	# test assumes pid values from shooter.py 
	# (kP=0.5, kI=0.02, kD=0.001, setpoint=0.3), dt=0.01
	def test_activate_carrier(self):
		print('test_activate_carrier()')
	
		# test_vals[0][0] is fake motor speed input, test_vals[0][1] is
		# expected update to motor speed from pid loop
		#XXX This will not work because the pid values we are testing are not
		# passed in to the carrier so the actual output will not equal supposed
		#XXX Tried to make it so it passes in pid values to class
		# but the class is instantiated in robotpy and its all confusing
		test_vals = [[0.2, 0.05002], [0.4, -0.05002]]
		for each in test_vals:
			motor_input = each[0]
			error = setpoint - motor_input
			d_input = 0
			proportional = kP * error # XXX self.XXX
			integral = kI * error * dt # XXX
			derivative = -kD * d_input / dt # XXX

			#actual_output = each[1]
			self.param.carrier
			actual_output = self.param.carrier_motor.get()
			supposed_output = proportional + integral + derivative
			# Rounds to four decimals so that assertion is exactly equal
			assert(round(actual_output, 4) == round(supposed_output, 4))

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
