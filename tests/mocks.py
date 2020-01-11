# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import sys
sys.path.append('./../commands')
sys.path.append('./../subsystems')
sys.path.append('./../')
from unittest import mock

def mock_drivetrain():
	with mock.patch('drivetrain.Drivetrain') as b:
		drivetrain_instance = b.return_value
	return drivetrain_instance

def mock_robot():
	with mock.patch('robot.BeaverTronicsRobot') as a:
		robot_instance = a.return_value 
		robot_instance.drivetrain = mock_drivetrain()
	return robot_instance




