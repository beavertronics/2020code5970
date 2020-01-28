#!/usr/bin/env python3
# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.command import Scheduler
from wpilib.buttons.joystickbutton import JoystickButton
import time
from networktables import NetworkTables

# Non robot specific libraries
import os
import sys
import math

#Linux path
sys.path.append('./subsystems') 
sys.path.append('./commands') 
sys.path.append('./tests')

#RoboRIO path
sys.path.insert(0, '/home/lvuser/py/subsystems')
sys.path.insert(0, '/home/lvuser/py/commands')

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season
from left_motors import Left_Motors
from right_motors import Right_Motors
from shifters import Shifters
from shooter import Shooter
from shooter_encoder import Shooter_Encoder
from intake import Intake

from drivetrain import Drivetrain

# Teleop init command
from oi import OI

# For testing
import unittest
from parametrized import ParametrizedTestCase
from test_do_tank_drive import Test_Do_Tank_Drive
from test_shifters import Test_Shifters
from test_shooter import Test_Shooter
from test_shooter_encoder import Test_Shooter_Encoder
from test_intake import Test_Intake

from test_drivetrain import Test_Drivetrain

class BeaverTronicsRobot(wpilib.TimedRobot): 

	def robotInit(self):
		# Instances of classes

		# Instantiate Subsystems
		self.shifters = Shifters()
		self.drivetrain = Drivetrain(self)
		self.shooter = Shooter(self)
		self.intake = Intake(self)

		# Instantiate Joysticks
		self.left_joy = wpilib.Joystick(0) 
		self.right_joy = wpilib.Joystick(1)
		
		# Instantiate Xbox
		self.xbox = wpilib.Joystick(2)

		# Instantiate OI; must be AFTER joysticks are inited
		self.oi = OI(self)

		self.timer = wpilib.Timer()
		self.loops = 0

		# untested vision
		#XXX might crash sim
		#wpilib.CameraServer.launch("vision.py:main")
		
	def autonomousInit(self):
		Scheduler.getInstance().removeAll()
		data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		
	def autonomousPeriodic(self):
		Scheduler.getInstance().run()

	def teleopInit(self):
		self.loops = 0
		self.timer.reset()
		self.timer.start()
		Scheduler.getInstance().removeAll()
		Scheduler.getInstance().enable()

	def teleopPeriodic(self):
		Scheduler.getInstance().run()

		# Keeping track of TimedRobot loops through code
		self.loops += 1
		if self.timer.hasPeriodPassed(1):
			self.logger.info("%d loops / second", self.loops)
			self.loops = 0

	def disabledInit(self):
		Scheduler.getInstance().removeAll()

	def disabledPeriodic(self):
		return None

	def testInit(self):
		return None

	def testPeriodic(self):
		suite = unittest.TestSuite()
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Shifters, param=self.shifters))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Shooter, param=self.shooter))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Drivetrain, param=self.drivetrain))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Shooter_Encoder, param=self.shooter.shooter_encoder))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Intake, param=self.intake))
		# TextTestRunner just outputs to stdout what is happening
		unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
