# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock
from parametrized import ParametrizedTestCase
import unittest
import wpilib
from drivetrain import Drivetrain
from left_motors import Left_Motors
from right_motors import Right_Motors

class Test_Drivetrain(ParametrizedTestCase):

	@classmethod
	def setUpClass(cls):
		print('setUpClass()')

	def setUp(self):
		print('setUp()')

		# Is getting this class from robot.py file
		with mock.patch('robot.BeaverTronicsRobot') as a:
			self.robot_instance = a.return_value		
			#XXX NOT WORKING, need to mock the joystick functions return vals
			#self.left_joy = self.robot_instance.left_joy.getY().return_value
			#self.right_joy = self.robot_instance.\
			#	right_joy.getY().return_value
			#XXX NOT WORKING
			#self.left_joy.getY() = -1
			#self.right_joy.getY() = 0

#		self.left_motors = Left_Motors()
#		self.right_motors = Right_Motors()
#
#		self.dt = Drivetrain(robot_instance)
#
#	def test_set_drivetrain_type(self):
#		print('test_set_drivetrain_type()')
#		assert(self.param.set_drivetrain_type(
#			wpilib.drive.DifferentialDrive, 
#			self.robot_instance.left_motors, self.robot_instance.right_motors\
#			== wpilib.drive.DifferentialDrive(
#				self.left_motors, self.right_motors)
#			))

	def test_set_tank_speed(self):
		#self.param.set_tank_speed(-1, 0)	
		self.param.set_tank_speed(self.left_joy, self.right_joy)
		assert(self.param.left_motors_instance.get() == -1)
		assert(self.param.right_motors_instance.get() == 0)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
