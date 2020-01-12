# vim: set sw=4 noet ts=4 fileencoding=utf-8:import sys

import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock
import unittest
from drivetrain import Drivetrain

class Test_Drivetrain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')

    def setUp(self):
        print('setUp()')

        with mock.patch('robot.BeaverTronicsRobot') as a:
            robot_instance = a.return_value        
                
        self.dt = Drivetrain(robot_instance)
        
    def test_set_drivetrain_type(self):
        print('test_set_drivetrain_type()')
        assert(self.dt.set_drivetrain_type(DifferentialDrive, self.left_motors, self.right_motors) == DifferentialDrive(self.left_motors, self.right_motors))

    def tearDown(self):
        print('tearDown()')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass()')

if __name__ == '__main__':
    unittest.main()
