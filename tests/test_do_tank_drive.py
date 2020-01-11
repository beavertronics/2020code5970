# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from do_tank_drive import Do_Tank_Drive
from unittest import mock
import unittest
import mocks

class Test_Do_Tank_Drive(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setUpClass()')

	def setUp(self):
		print('setUp()')
		robot_instance = mocks.mock_robot()
		#with mock.patch('robot.BeaverTronicsRobot') as a:
			#robot_instance = a.return_value
		#with mock.patch('drivetrain.Drivetrain') as b:
		#	drivetrain_instance = b.return_value
		#robot_instance.drivetrain = drivetrain_instance
		self.td = Do_Tank_Drive(robot_instance)

	def test_isFinished(self):
		print('test_isFinished()')
		assert(self.td.isFinished() == False)

	def tearDown(self):
		print('setUp()')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass()')

if __name__ == '__main__':
	unittest.main()
