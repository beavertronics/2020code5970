# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
#from unittest import mock
import unittest
from unittest.mock import patch
from parametrized import ParametrizedTestCase
import wpilib
from drivetrain import Drivetrain
from left_motors import Left_Motors
from right_motors import Right_Motors

class Test_Drivetrain(ParametrizedTestCase):

	@classmethod
	def setUpClass(cls):
		print('setUpClass()')
		print('param = BeaverTronicsRobot.drivetrain')

	def setUp(self):
		print('setUp()')
		with patch('drivetrain.Drivetrain') as mock:
			dt_inst = mock.return_value
			self.drive_inst = dt_inst.drive

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
		self.left_joy = wpilib.Joystick(0)
		self.right_joy = wpilib.Joystick(1)

	@patch('wpilib.Joystick')	
	@patch('wpilib.Joystick')
	def test_set_tank_speed(self, mock_left_joy, mock_right_joy):
		''' Passes in fake values and mocks the behavior of joysticks to test
			if the speed is set correctly '''
		mock_left_joy.getY.return_value = -1.0
		mock_right_joy.getY.return_value = 0.0
		self.param.set_tank_speed(
			left_joy=mock_left_joy, right_joy=mock_right_joy, 
			drive=self.drive_inst)
		print(mock_left_joy.getY)
		print(mock_right_joy)
		print("Left_motors: " + str(self.param.left_motors.get()))
		assert(self.param.left_motors.get() == -1.0)
		assert(self.param.right_motors.get() == 0.0)

	def tearDown(self):
		print('tearDown()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
