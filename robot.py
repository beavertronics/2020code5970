#!/usr/bin/env python3
# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.command import Scheduler
from wpilib.buttons import JoystickButton
import time
from networktables import NetworkTables
from commandbased.commandbasedrobot import CommandBasedRobot

# Non robot specific libraries
import os
import sys
import math

#Linux path
sys.path.append('./subsystems') 
sys.path.append('./commands') 
sys.path.append('./tests')
sys.path.append('./vision')

#RoboRIO path
sys.path.insert(0, '/home/lvuser/py/subsystems')
sys.path.insert(0, '/home/lvuser/py/commands')
sys.path.insert(0, '/home/lvuser/py/tests')
sys.path.insert(0, '/home/lvuser/py/vision')

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season
from shooter import Shooter
from feeder import Feeder
from carrier import Carrier
from intake import Intake
from winch import Winch
#from climber import Climber
from climber_big import Climber_Big
from climber_little import Climber_Little

from drivetrain import Drivetrain

# Teleop init command
from oi import OI

# For testing
import unittest
from parametrized import ParametrizedTestCase
from test_do_tank_drive import Test_Do_Tank_Drive
#from test_shooter import Test_Shooter
#from test_shooter_encoder import Test_Shooter_Encoder
from test_feeder import Test_Feeder
from test_carrier import Test_Carrier
from test_intake import Test_Intake
from test_winch import Test_Winch
from test_climber import Test_Climber
from test_drivetrain import Test_Drivetrain

# Auto Commands
from command_bad_auto import Command_Bad_Auto

class BeaverTronicsRobot(CommandBasedRobot): 

	def robotInit(self):
		super().__init__()
		# Instances of classes

		# Instantiate Subsystems
		#XXX DEBUGGING
		self.drivetrain = Drivetrain(self)
		self.shooter = Shooter(self)
		self.carrier = Carrier(self)
		self.feeder = Feeder(self)
		self.intake = Intake(self)
		self.winch = Winch(self)
		#self.climber = Climber(self)
		self.climber_big = Climber_Big(self)
		self.climber_little = Climber_Little(self)

		# Instantiate Joysticks
		self.left_joy = wpilib.Joystick(0) 
		self.right_joy = wpilib.Joystick(1)
		# Instantiate Xbox
		self.xbox = wpilib.Joystick(2)

		# Instantiate OI; must be AFTER joysticks are inited
		self.oi = OI(self)

		self.timer = wpilib.Timer()

		# untested vision
		#wpilib.CameraServer.launch("vision.py:main")
		#wpilib.CameraServer.launch()
		
	def autonomousInit(self):
		# Scheduler.getInstance().removeAll()
		data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		
	def autonomousPeriodic(self):
		Scheduler.getInstance().addCommand(Command_Bad_Auto(self))
		Scheduler.getInstance().run()

	def teleopInit(self):
		pass

	def teleopPeriodic(self):
		Scheduler.getInstance().run()
		self.logger.info(self.getPeriod())

	def disabledInit(self):
		pass

	def disabledPeriodic(self):
		pass

	def testInit(self):
		return None

	def testPeriodic(self):
		suite = unittest.TestSuite()
		#suite.addTest(ParametrizedTestCase.parametrize(
		#	Test_Shooter, param=self.shooter))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Drivetrain, param=self.drivetrain))
		#suite.addTest(ParametrizedTestCase.parametrize(
		#	Test_Shooter_Encoder, param=self.shooter.shooter_encoder))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Feeder, param=self.feeder))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Carrier, param=self.carrier))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Intake, param=self.intake))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Winch, param=self.winch))
		suite.addTest(ParametrizedTestCase.parametrize(
			Test_Climber, param=self.climber))
		# TextTestRunner just outputs to stdout what is happening
		unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
